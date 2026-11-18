
# main.py - Raspberry Pi Pico 2
# Simplified mission controller

from config import *
from motors import Motors
from navigation import Navigation
from sensors import Ultrasonic
from deployment import Stepper_deployer
from lights import Lights

WAITING = 0
DEPLOYING = 1
LANDED = 2
SEARCHING = 3
ALIGNING = 4
APPROACHING = 5
COMPLETE = 6
ERROR = 7

state = WAITING

# Hardware objects will be initialized here:
motors = Motors()
ultrasonic = Ultrasonic()
deployment = Stepper_deployer()
lights = Lights(False)
navigation = Navigation(motors)
# navigation = Navigation(motors)
# deployment = Deployment(...)
# sensors = Sensors(...)
# camera = CameraComm(...)
# lights = Lighting(...)

def update_mission():
    global state

    if state == WAITING:
        if mission_started():
            state = DEPLOYING

    elif state == DEPLOYING:
        altitude = ultrasonic.update()
        

        if ultrasonic.landed:
            state = LANDED
            

    elif state == LANDED:
        deployment.full_extend()

        if deployment.isready:
            lights.on()
            state = SEARCHING
            
    elif state == SEARCHING:
        navigation.search()

        if camera.tag_visible():
            motors.stop()
            state = ALIGNING

    elif state == ALIGNING:
        if not camera.tag_visible():
            motors.stop()
            state = SEARCHING

        elif navigation.align(camera.tag_x()):
            state = APPROACHING

    elif state == APPROACHING:
        if not camera.tag_visible():
            motors.stop()
            state = SEARCHING

        elif not camera.is_fresh():
            motors.stop()
            state = ERROR

        elif navigation.approach(camera.distance_cm()):
            state = COMPLETE

    elif state == COMPLETE:
        motors.stop()

    elif state == ERROR:
        motors.stop()
        lights.on()

while True:
    update_mission()
        
