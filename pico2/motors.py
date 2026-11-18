"""TB6612FNG two-channel differential drive for MicroPython on Pico 2."""
from machine import Pin, PWM
from config import (AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY,
                    PWM_FREQUENCY_HZ, LEFT_INVERT, RIGHT_INVERT)

class Motors:
    def __init__(self):
        self._ain1 = Pin(AIN1, Pin.OUT, value=0)
        self._ain2 = Pin(AIN2, Pin.OUT, value=0)
        self._bin1 = Pin(BIN1, Pin.OUT, value=0)
        self._bin2 = Pin(BIN2, Pin.OUT, value=0)
        self._stby = Pin(STBY, Pin.OUT, value=0)
        self._pwma = PWM(Pin(PWMA), freq=PWM_FREQUENCY_HZ)
        self._pwmb = PWM(Pin(PWMB), freq=PWM_FREQUENCY_HZ)
        self._pwma.duty_u16(0)
        self._pwmb.duty_u16(0)
        self._stby.value(1)

    @staticmethod
    def _clamp(speed):
        return max(-1.0, min(1.0, float(speed)))

    @staticmethod
    def _drive(pin1, pin2, pwm, speed):
        speed = Motors._clamp(speed)
        # Remove PWM drive before switching direction.
        pwm.duty_u16(0)
        if speed > 0:
            pin1.value(1)
            pin2.value(0)
        elif speed < 0:
            pin1.value(0)
            pin2.value(1)
        else:
            pin1.value(0)
            pin2.value(0)
        pwm.duty_u16(round(abs(speed) * 65535))

    def set_speeds(self, left, right):
        if LEFT_INVERT:
            left = -left
        if RIGHT_INVERT:
            right = -right
        self._drive(self._ain1, self._ain2, self._pwma, left)
        self._drive(self._bin1, self._bin2, self._pwmb, right)

    def forward(self, speed=0.25):
        self.set_speeds(speed, speed)

    def backward(self, speed=0.25):
        self.set_speeds(-speed, -speed)

    def turn_left(self, speed=0.25):
        self.set_speeds(-speed, speed)

    def turn_right(self, speed=0.25):
        self.set_speeds(speed, -speed)

    def stop(self):
        # Both input pins low: coast stop on TB6612FNG.
        self.set_speeds(0, 0)

    def disable(self):
        self.stop()
        self._stby.value(0)

    def enable(self):
        self._stby.value(1)

    def deinit(self):
        self.disable()
        self._pwma.deinit()
        self._pwmb.deinit()
