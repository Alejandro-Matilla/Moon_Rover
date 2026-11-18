from lights import Lights
import time


lights = Lights(False)

while True:
    lights.on
    time.sleep_us(100)
    lights.off
