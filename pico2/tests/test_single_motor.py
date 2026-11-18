
from machine import Pin, PWM
import time

# Motor A on TB6612FNG
ain1 = Pin(2, Pin.OUT)
ain2 = Pin(3, Pin.OUT)
pwma = PWM(Pin(4))
stby = Pin(9, Pin.OUT)

pwma.freq(20000)
pwma.duty_u16(0)
stby.value(1)

try:
    print("Forward")
    ain1.value(1)
    ain2.value(0)
    pwma.duty_u16(int(32768/3))  # 50% PWM
    time.sleep(2)

    print("Stop")
    pwma.duty_u16(0)
    time.sleep(1)

    print("Backward")
    ain1.value(0)
    ain2.value(1)
    pwma.duty_u16(int(32768/3))
    time.sleep(2)

finally:
    pwma.duty_u16(0)
    ain1.value(0)
    ain2.value(0)
    stby.value(0)
    pwma.deinit()
    print("Motor test complete")
