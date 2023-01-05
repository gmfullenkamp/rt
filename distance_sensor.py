from gpiozero import DistanceSensor
from time import sleep


distance_sensor = DistanceSensor(23, 24)

while True:
    print("Distance to nearest object is", distance_sensor.distance, "m")
    sleep(1)
