# Code for the ultrasonic range finder
ULTRASONIC_TRIG = 10
ULTRASONIC_ECHO = 11
ULTRASONIC_INTERVAL_MS = 60
ULTRASONIC_TIMEOUT_US = 30000
LANDING_HEIGHT_CM = 30.0
LANDING_CONFIRMATIONS = 3

# Defining constants for the stepper motor deploymenr
STEPPER_CHANNEL_A = 12
STEPPER_CHANNEL_B = 13
STEPPER_CHANNEL_C = 14
STEPPER_CHANNEL_D = 15
SEQUENCE_FULL_STEP = [
    (1,0,0,0),
    (0,1,0,0),
    (0,0,1,0),
    (0,0,0,1)
]
SEQUENCE_HALF_STEP = [
    (1,0,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,1,1,0),
    (0,0,1,0),
    (0,0,1,1),
    (0,0,0,1),
    (1,0,0,1)
]

DEGREES = 180
DEGREES_PER_STEP_FULLSTEP = 360/200
DEGREES_PER_STEP_HALFSTEP = 360/400
RPMS = 20
DEGREES_CHOSEN = DEGREES_PER_STEP_FULLSTEP
STEPS = DEGREES/DEGREES_CHOSEN
DELAY = DEGREES_CHOSEN * 60 / (360 * RPMS)

# Constants for the LEDs
LED = 16

# Pico 2 GPIO mapping for TB6612FNG
AIN1 = 2
AIN2 = 3
PWMA = 4
BIN1 = 6
BIN2 = 7
PWMB = 8
STBY = 9
PWM_FREQUENCY_HZ = 20000
# Flip either direction if its side drives backwards.
# Code for the search and align
LEFT_INVERT = False
RIGHT_INVERT = False
IMAGE_WIDTH = 200
ALIGNMENT_TOLERANCE_PX = 10
ALIGN_SPEED = 0.5
SEARCH_SPEED = 0.2
APPROACH_SPEED = 0.1



from machine import Pin
import time

# Configure GPIO pin (e.g., pin 15) as an output
led = Pin(15, Pin.OUT)

# Turn the LED on
led.on()  # or led.value(1)

# Wait for 2 seconds
time.sleep(2)

# Turn the LED off
led.off()  # or led.value(0)


        
        
    
    
    


