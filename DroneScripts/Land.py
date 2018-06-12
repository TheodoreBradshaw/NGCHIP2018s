from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)
vehicle = connect('10.1.1.165:14550', wait_ready=True)
vehicle.armed = True
vehicle.groundspeed = 3
vehicle.airspeed = 3
time.sleep(1)
vehicle.mode = VehicleMode("RTL")
time.sleep(3)
vehicle.close()
