import time
from connect import connectMyCopter
from photo_shot import photo
from take_off import arm_and_takeoff
from land import land


def start_mission(high):

    vehicle = connectMyCopter()
    print("About to takeoff..")
    arm_and_takeoff(vehicle, high)
    while vehicle.attitude <= high - 0.5:
        continue
    time.sleep(15)
    photo("prob", 1)
    time.sleep(10)
    land(vehicle)
    print("END")
    vehicle.close()

if __name__ == "__main__":
    high = 1
    start_mission(high)
