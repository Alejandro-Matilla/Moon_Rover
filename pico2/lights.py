from machine import Pin
from config import LED
import time
from time import ticks_us, ticks_diff

class Lights:
    def __init__(self, aura):
        self._pin = Pin(LED, Pin.OUT, value = 0)
        self._aura = aura
        self._state = True # True for On, False for Offf



    # Additional functionality not finished
    # def aura(self):
    #     self.aura()
    #     self._pin.high()
    #     time_now = ticks_us
    #     if ticks_diff(time.,time_now) > 150:

    def on(self):
        if not self._aura:
            self._pin.high()

    def off(self):
        if self._state:
            self._pin.off()
    
        

