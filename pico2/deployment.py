from machine import Pin
import time
from config import (
    STEPPER_CHANNEL_A,
    STEPPER_CHANNEL_B,
    STEPPER_CHANNEL_C,
    STEPPER_CHANNEL_D,
    STEPS,
    DELAY,
    SEQUENCE_FULL_STEP,
    SEQUENCE_HALF_STEP


)

class Stepper_deployer:
    def __init__(self):
        self._channelA = Pin(STEPPER_CHANNEL_A, Pin.OUT, value=0)
        self._channelB = Pin(STEPPER_CHANNEL_B, Pin.OUT, value=0)
        self._channelC = Pin(STEPPER_CHANNEL_C, Pin.OUT, value=0)
        self._channelD = Pin(STEPPER_CHANNEL_D, Pin.OUT, value=0)
        self.isready = False
        self._steps = int(STEPS)
        self._delay = DELAY
        self._sequence = SEQUENCE_FULL_STEP
        self._pins =  [self._channelA, self._channelB, self._channelC, self._channelD]


    def full_extend(self):
        for i in range(self._steps):
            pattern = self._sequence[i % 8]

            for pin, value in zip(self._pins, pattern):
                pin.value(value)

            time.sleep(self._delay)

        self._isready = True

