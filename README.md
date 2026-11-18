# Lunar South Pole Exploration Rover

## Overview
This project develops a small autonomous rover that simulates exploration of the Moon's south pole in a dark environment. The rover is lowered to the ground, detects landing, deploys its camera, illuminates the surroundings, searches for an AprilTag, and drives toward the detected target.

## Hardware
- **Raspberry Pi Pico 2:** Main rover controller, programmed in MicroPython
- **OpenMV camera:** Vision processing and AprilTag detection
- **TB6612FNG motor drivers:** Drive motors and bipolar stepper control (separate driver channels required)
- **Ultrasonic rangefinder:** Measures distance to the ground for landing detection
- **Stepper-driven deployment mechanism:** Extends the camera after landing
- **Lights:** Illuminate the camera's field of view
- **Four-wheel chassis:** Rover mobility

## Mission Sequence
1. Monitor the ultrasonic rangefinder while the rover is lowered.
2. Detect when the rover has landed.
3. Run the camera deployment stepper sequence to completion.
4. Turn on the camera lights.
5. Rotate the rover to search for an AprilTag.
6. Drive toward the detected AprilTag.

## Software Structure
The planned MicroPython codebase separates hardware control and mission logic:

```text
main.py       # Main program and mission sequence
config.py     # GPIO assignments and system constants
motors.py     # Wheel motor control using TB6612FNG
stepper.py    # Camera deployment stepper sequences
sensors.py    # Ultrasonic rangefinder and landing detection
```

The OpenMV camera runs its own vision code and communicates detection results to the Pico 2. File names and interfaces may evolve as the project is implemented.

## Control Approach
Camera deployment can use a **blocking stepper sequence**, since other rover operations are not required during this stage. After deployment finishes, the controller turns on the lights and proceeds to vision-based navigation.

## Future Functionality
- **Train a machine-learning model** to recognize different objects that may appear on the Moon's surface, such as rocks, craters, and potential obstacles.
- **Implement object-specific responses:** for example, navigate around obstacles, investigate scientifically interesting objects, or stop when hazardous terrain is detected.
- Improve autonomous navigation and decision-making based on camera detections.

## Project Status
Under development. Hardware interfaces, motor control, landing detection, camera deployment, and autonomous navigation are being implemented and tested.
