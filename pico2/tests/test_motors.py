"""Run on Pico 2 with wheels lifted. Press Ctrl+C to stop."""
import time
from motors import Motors

motors = Motors()
try:
    print('Forward')
    motors.forward(0.25)
    time.sleep(1)
    motors.stop()
    time.sleep(1)

    print('Backward')
    motors.backward(0.25)
    time.sleep(1)
    motors.stop()
    time.sleep(1)

    print('Turn left')
    motors.turn_left(0.25)
    time.sleep(1)
    motors.stop()
    time.sleep(1)

    print('Turn right')
    motors.turn_right(0.25)
    time.sleep(1)
    motors.stop()
    print('Test complete')
finally:
    motors.deinit()
