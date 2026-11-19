from deployment import Stepper_deployer 
from sensors import Ultrasonic
from lights import Lights
import time

stepper = Stepper_deployer()
stepper.full_extend()