import time
from connect import connectMyCopter
from dronekit import VehicleMode
from take_off import arm_and_takeoff


def start_mission():
    vehicle = connectMyCopter()
    print("About to takeoff..")

    arm_and_takeoff(1)
    time.sleep(2)
    vehicle.mode = VehicleMode("LAND")


    print("END")

    vehicle.close()

if __name__ == "__main__":
    start_mission()
