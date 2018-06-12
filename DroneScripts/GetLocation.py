from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)
vehicle = connect('10.1.1.165:14550', wait_ready=True)

print "Global Location: %s" % vehicle.location.global_frame
print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
print "Local Location: %s" % vehicle.location.local_frame
vehicle.close()



