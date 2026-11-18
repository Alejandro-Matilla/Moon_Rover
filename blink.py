from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)
pin2 = Pin(15, Pin.OUT)

print("LED starts flashing...")
try:
    while True:
        led.toggle()
        pin2.toggle()
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    led.off()
    pin2.off()
    print("Finished.")