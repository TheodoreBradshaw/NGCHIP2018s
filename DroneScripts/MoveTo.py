from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)
vehicle = connect('10.1.1.165:14550', wait_ready=True)

vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
home_new = LocationGlobal(39.3038813,-84.4778206,223) # Make sure altitude is a decent amount above the ground
time.sleep(1)
vehicle.airspeed = 2 # Adjust these two numbers (M/S) as you please, higher is faster. 3 is a definite safe, slow speed
vehicle.groundspeed = 2
vehicle.simple_goto(home_new)
my_location = home_new
print my_location
my_location.alt = 210 # Make this a number that is slightly below the ground
vehicle.home_location = my_location
time.sleep(5) # Increases for longer travel distances
vehicle.airspeed = 3 # Generally safe landing speed
vehicle.groundspeed = 3
vehicle.mode = VehicleMode("RTL") # Go to home
time.sleep(14) # Do I need this sleep? Probably not. But why not? Probably some good reasons.
vehicle.close()
