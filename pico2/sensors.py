
"""Interrupt-driven ultrasonic sensor for Pico 2."""

from machine import Pin
import time

from config import (
    ULTRASONIC_TRIG,
    ULTRASONIC_ECHO,
    ULTRASONIC_INTERVAL_MS,
    ULTRASONIC_TIMEOUT_US,
    LANDING_HEIGHT_CM,
    LANDING_CONFIRMATIONS
)


class Ultrasonic:
    def __init__(self):
        self._trig = Pin(
            ULTRASONIC_TRIG, Pin.OUT, value=0
        )
        self._echo = Pin(
            ULTRASONIC_ECHO, Pin.IN
        )

        self._start_us = 0
        self._pulse_us = 0
        self._state = 0
        self._last_trigger_ms = time.ticks_ms()

        self.distance_cm = 1000
        self.landed = False
        self._confirmations = 0

        # Interrupt on rising and falling edges
        self._echo.irq(
            trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
            handler=self._echo_irq
        )

    def _echo_irq(self, pin):
        """Capture echo timing; keep IRQ very short."""

        if self._state == 1 and pin.value():
            # Echo pulse begins
            self._start_us = time.ticks_us()
            self._state = 2

        elif self._state == 2 and not pin.value():
            # Echo pulse ends
            self._pulse_us = time.ticks_diff(
                time.ticks_us(),
                self._start_us
            )
            self._state = 3

    def update(self):
        """Call frequently from the main loop."""

        now = time.ticks_ms()

        # Process a completed measurement
        if self._state == 3:
            pulse = self._pulse_us
            self._state = 0

            if 100 <= pulse <= ULTRASONIC_TIMEOUT_US:
                self.distance_cm = pulse * 0.0343 / 2
                self._check_landing()
            else:
                self.distance_cm = 1000
                self._confirmations = 0

        # Handle missing echo / timeout
        elif self._state in (1, 2):
            elapsed = time.ticks_diff(
                time.ticks_us(),
                self._measurement_start_us
            )

            if elapsed > ULTRASONIC_TIMEOUT_US:
                self._state = 0
                self.distance_cm = 1000
                self._confirmations = 0

        # Start next measurement
        if self._state == 0:
            if time.ticks_diff(
                now, self._last_trigger_ms
            ) >= ULTRASONIC_INTERVAL_MS:

                # Do not trigger if echo is still HIGH
                if self._echo.value():
                    return

                self._state = 1
                self._measurement_start_us = time.ticks_us()
                self._last_trigger_ms = now

                self._trig.value(1)
                time.sleep_us(10)
                self._trig.value(0)

    def _check_landing(self):
        """Require consecutive low-height readings."""

        if self.distance_cm <= LANDING_HEIGHT_CM:
            self._confirmations += 1
            print(self.distance_cm)
        else:
            self._confirmations = 0

        if self._confirmations >= LANDING_CONFIRMATIONS:
            self.landed = True

    def reset_landing(self):
        self.landed = False
        self._confirmations = 0

    def deinit(self):
        self._echo.irq(handler=None)
        self._trig.value(0)
