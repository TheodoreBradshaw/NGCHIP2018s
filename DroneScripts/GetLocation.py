from dronekit import connect

vehicle = connect('udpin:0.0.0.0:14550', wait_ready=True)

print [vehicle.location.global_frame.lat, vehicle.location.global_frame.lon, vehicle.location.global_frame.alt]
vehicle.close()
