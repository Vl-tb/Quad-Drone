from dronekit import Vehicle, LocationGlobal

def move(coord1, coord2, vehicle: Vehicle):
    a_location = LocationGlobal(coord1, coord2, 5)
    vehicle.simple_goto(a_location)