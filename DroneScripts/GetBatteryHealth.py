from dronekit import connect
vehicle = connect('udpin:0.0.0.0:14550', wait_ready=True)
print vehicle.battery
vehicle.close()
