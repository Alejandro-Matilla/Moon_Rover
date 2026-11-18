from sensors import Ultrasonic

ultrasonic = Ultrasonic()
while True:
    print(ultrasonic.distance_cm)
    ultrasonic.update()
    ultrasonic._check_landing()