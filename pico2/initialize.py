from machine import Pin
from config import BUTTON, PULLUP

button_pin = Pin(BUTTON, Pin.IN, value = 0)
pullup_cond = PULLUP

def mission_started():
    if button_pin.high():
        return True

    else:
        return False



