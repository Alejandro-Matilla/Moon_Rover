from machine import Pin
from config import BUTTON, PULLUP

button_pin = Pin(BUTTON, Pin.IN, Pin.PULL_DOWN)

pullup_cond = PULLUP

def mission_started():
    if button_pin.high():
        return True

    else:
        return False



