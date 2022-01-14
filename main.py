import time
from connect import connectMyCopter
from photo_shot import photo
from take_off import arm_and_takeoff
from land import land
from photo_coords import find_coordinates
from read_coords import read
from current_coords import getCoords
from merge_main import main
from a_b import move


def start_mission(high):
    edges = read()
    coords = find_coordinates(edges, high)


    base_coords = getCoords()
    vehicle = connectMyCopter()
    print("About to takeoff..")
    arm_and_takeoff(vehicle, high)
    while vehicle.attitude <= high - 0.5:
        continue
    time.sleep(15)
    a = len(coords[0])+1
    b = 1
    param = 1
    for i in range(len(coords)):
        for j in range(b, a, param):
            move(coords[i][j-1][0], coords[i][j-1][1], vehicle)
            while ((abs(getCoords()[0] - coords[i][j-1][0])>= 0.00001) and
                (abs(getCoords()[0] - coords[i][j-1][0])>= 0.00001)):
                continue
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
