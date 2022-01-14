import time
from connect import connectMyCopter
from take_off import arm_and_takeoff
from land import land
from coords_finder import find_center
from read_coords import read
from current_coords import getCoords
from a_b import move
from yaw_set import condition_yaw


def start_mission(high):
    edges = read()
    coords = find_center(edges[0], edges[1], edges[2], high)


    base_coords = getCoords()
    target_coords = [base_coords[0] + 0.00001, base_coords[1]]
    vehicle = connectMyCopter()
    print("About to takeoff..")
    arm_and_takeoff(vehicle, high)
    while vehicle.attitude <= high - 0.5:
        continue
    time.sleep(15)

    move(target_coords[0], target_coords[1], vehicle)
    while ((abs(getCoords()[0] - target_coords[0])>= 0.00001) and
                (abs(getCoords()[0] - target_coords[1])>= 0.00001)):
        continue
    time.sleep(10)
    condition_yaw(0, vehicle) #heading North
    time.sleep(10)

    move(base_coords[0], base_coords[1], vehicle)
    while ((abs(getCoords()[0] - base_coords[0])>= 0.00001) and
                (abs(getCoords()[0] - base_coords[1])>= 0.00001)):
        continue
    time.sleep(15)

    land(vehicle)
    print("END")
    vehicle.close()

if __name__ == "__main__":
    high = 1
    start_mission(high)
