from deployment import Stepper_deployer 
from sensors import Ultrasonic
from lights import Lights
import time

stepper = Stepper_deployer()
ultra = Ultrasonic()
led = Lights()

while True:
    ultra.update()
    ultra._check_landing()
    if not ultra.landed:
        print("Not landed")

    if ultra.landed and not stepper.isready:
        print("Landed, proceeding with extension")
        stepper.full_extend()

    if stepper.isready:
        print("Finished extension, turning LEDs on")
        led.on()
        break

    time.sleep_ms(100)

time.sleep_ms(2000)
led.off()
print("Changing state into searching")