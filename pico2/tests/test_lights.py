from lights import Lights
from sensors import Ultrasonic

import time


lights = Lights(False)
ultra = Ultrasonic()
  
while True:
    ultra.update()
    ultra._check_landing()
    print("NOT LANDED")
    lights.on()  
    if ultra.landed:
        lights.off()
        print("LANDED")  
        break

    time.sleep_ms(100)
