import time
from connect import connectMyCopter
from photo_shot import photo
from take_off import arm_and_takeoff
from land import land
from coords_finder import find_center
from read_coords import read
from current_coords import getCoords
from merge_main import main
from a_b import move
from yaw_set import condition_yaw


def start_mission(high):
    edges = read()
    coords = find_center(edges[0], edges[1], edges[2], high)


    base_coords = getCoords()
    vehicle = connectMyCopter()
    print("About to takeoff..")
    arm_and_takeoff(vehicle, high)
    while vehicle.attitude <= high - 0.5:
        continue
    time.sleep(15)

    move(edges[0][0], edges[0][1], vehicle)
    while ((abs(getCoords()[0] - edges[0][0])>= 0.00001) and
                (abs(getCoords()[0] - edges[0][1])>= 0.00001)):
        continue
    time.sleep(10)
    move(edges[2][0], edges[2][1], vehicle)
    while ((abs(getCoords()[0] - edges[2][0])>= 0.00001) and
                (abs(getCoords()[0] - edges[2][1])>= 0.00001)):
        continue
    time.sleep(10)

    bearing = vehicle.attitude.yaw

    a = len(coords[0])+1
    b = 1
    param = 1
    for i in range(len(coords)):
        for j in range(b, a, param):
            move(coords[i][j-1][0], coords[i][j-1][1], vehicle)
            while ((abs(getCoords()[0] - coords[i][j-1][0])>= 0.00001) and
                (abs(getCoords()[0] - coords[i][j-1][0])>= 0.00001)):
                continue
            time.sleep(5)
            condition_yaw(bearing, vehicle)
            time.sleep(15)
            photo(i, j)
        a, b = b, a
        param = -1*param
        a += param
        b += param
    main()
    move(base_coords[0], base_coords[1], vehicle)
    while ((abs(getCoords()[0] - base_coords[0])>= 0.00001) and
                (abs(getCoords()[0] - base_coords[1])>= 0.00001)):
        continue
    time.sleep(15)

    land(vehicle)
    print("END")
    vehicle.close()

if __name__ == "__main__":
    high = 30
    start_mission(high)
