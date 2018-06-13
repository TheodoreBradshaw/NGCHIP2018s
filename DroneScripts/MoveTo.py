from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
import sys
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)

# Vars
MyIP = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
TargetHomeGPS = [39.303190, -84.477859, 223]    # GPS Coordinate, make sure (3rd value) is relatively high above ground

TravelSpeed = 2   # integer, speed in m/s, Matt = [3, 5]
LandingSpeed = 2    # integer, speed in m/s, Matt = 3

# Connect
vehicle = connect(MyIP, wait_ready=True)
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

# Get all vehicle attributes (state)
print "Vehicle state:"
print " Global Location: %s" % vehicle.location.global_frame
print " Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
print " Local Location: %s" % vehicle.location.local_frame
print " Attitude: %s" % vehicle.attitude
print " Velocity: %s" % vehicle.velocity
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Heading: %s" % vehicle.heading
print " Groundspeed: %s" % vehicle.groundspeed
print " Airspeed: %s" % vehicle.airspeed
print " Mode: %s" % vehicle.mode.name
print " Is Armable?: %s" % vehicle.is_armable
print " Armed: %s" % vehicle.armed

# Set Locations
print TargetHomeGPS
home_hover = LocationGlobal(TargetHomeGPS[0], TargetHomeGPS[1], TargetHomeGPS[2])
home_ground = LocationGlobal(TargetHomeGPS[0], TargetHomeGPS[1], TargetHomeGPS[2])
home_ground.alt = TargetHomeGPS[2] - 15   # Make this a number that is slightly below the ground
time.sleep(1)

# Change Home Location
vehicle.home_location = home_ground
time.sleep(1)

# Travel over New Home
vehicle.airspeed = TravelSpeed
vehicle.groundspeed = TravelSpeed
vehicle.simple_goto(home_hover)
time.sleep(5)    # Increases for longer travel distances

# Land
vehicle.airspeed = LandingSpeed    # Generally safe landing speed
vehicle.groundspeed = LandingSpeed
vehicle.mode = VehicleMode("RTL") # Go to home
time.sleep(14)  # Do I need this sleep? Probably not. But why not? Probably some good reasons.
vehicle.close()
