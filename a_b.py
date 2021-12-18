from dronekit import LocationGlobal

def move(coord1, coord2, vehicle):
    a_location = LocationGlobal(coord1, coord1, 5)
    vehicle.simple_goto(a_location)