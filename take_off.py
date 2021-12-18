import time
from dronekit import VehicleMode

def arm_and_takeoff(vehicle, meters):

    while not vehicle.is_armable:
        print("Waiting drone to become armable")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    while vehicle.mode != "GUIDED":
        print("Waiting for vehicle to enter Guided mode")
        time.sleep(1)
    
    vehicle.armed = True
    while vehicle.armed == False:
        print("Waiting drone to become armable")
        time.sleep(1)

    vehicle.simple_takeoff(meters)

    while True:
        print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= meters*0.95:
            break
        time.sleep(1)

    print("Its on position")

    return None