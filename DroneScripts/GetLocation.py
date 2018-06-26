from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)
vehicle = connect('udpin:0.0.0.0:14550', wait_ready=True)

print [vehicle.location.global_frame.lat, vehicle.location.global_frame.lon, vehicle.location.global_frame.alt]
vehicle.close()
