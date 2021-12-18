from dronekit import Vehicle, VehicleMode

def land(vehicle: Vehicle):
    vehicle.mode = VehicleMode("LAND")