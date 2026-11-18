
# navigation.py

from config import (
    IMAGE_WIDTH,
    ALIGNMENT_TOLERANCE_PX,
    ALIGN_SPEED,
    SEARCH_SPEED,
    APPROACH_SPEED
)

class Navigation:
    def __init__(self, motors):
        self.motors = motors

    def search(self):
        self.motors.turn_left(SEARCH_SPEED)

    def align(self, tag_x):
        center_x = IMAGE_WIDTH / 2
        error = tag_x - center_x

        if abs(error) <= ALIGNMENT_TOLERANCE_PX:
            self.motors.stop()
            return True

        if error > 0:
            self.motors.turn_right(ALIGN_SPEED)
        else:
            self.motors.turn_left(ALIGN_SPEED)

        return False

    def approach(self, distance_cm):
        if distance_cm <= 11.0:
            self.motors.stop()
            return True

        self.motors.forward(APPROACH_SPEED)
        return False
