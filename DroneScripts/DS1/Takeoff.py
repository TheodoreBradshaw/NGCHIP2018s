from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)
vehicle = connect('10.1.1.165:14550', wait_ready=True)
while not vehicle.is_armable:
	print"waiting"
	time.sleep(1)
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.groundspeed = 3
vehicle.airspeed = 3
time.sleep(5)
vehicle.simple_takeoff(8)
x=0
while vehicle.location.global_relative_frame.alt<=6:
	print "Rising..."
	time.sleep(1)
	x = x+1
	if x == 8:
		print "This simple takeoff is not so simple. Going Higher"		
		failure = vehicle.location.global_frame
		failure.alt = 225 # Adjust this altitude logically, 8 metres above takeoff point is generally good
		vehicle.simple_goto(failure)
		time.sleep(5)
		x = 0
print "Altitude reached"
vehicle.close()

