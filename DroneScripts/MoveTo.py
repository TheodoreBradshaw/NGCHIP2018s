from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
import sys
# Connect to the Vehicle (in this case a UDP endpoint)
# Insert YOUR ip address in the next line when connected to the drone's network (Bridged Connection, replicate in VM)

print "\n" + "*"*30 + "\n"
# Vars
# MyIP = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'     # Only works when on the right network.
MyIP = 'udpin:0.0.0.0:14550'     # Only works when on the right network.
TargetHomeGPS = [39.3031664, -84.4779333, 223]    # Hardcoded GPS Coordinate, this should be the input variable
# TargetHomeGPS = [39.302870, -84.477827, 233]   # Far downfield, backup coordinates.

# TravelSpeed = 3   # integer, speed in m/s, Matt = [3, 5]
# LandingSpeed = 2    # integer, speed in m/s, Matt = 3
#
# # Connect
#
# vehicle = connect(MyIP, wait_ready=True)
# vehicle.mode = VehicleMode("GUIDED")
# vehicle.armed = False
#
# # Get all vehicle attributes (state)
# print "Vehicle state:"
# print " Global Location: %s" % vehicle.location.global_frame
# print " Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
# print " Local Location: %s" % vehicle.location.local_frame
# print " Attitude: %s" % vehicle.attitude
# print " Velocity: %s" % vehicle.velocity
# print " Battery: %s" % vehicle.battery
# print " Last Heartbeat: %s" % vehicle.last_heartbeat
# print " Heading: %s" % vehicle.heading
# print " Ground speed: %s" % vehicle.groundspeed
# print " Airspeed: %s" % vehicle.airspeed
# print " Mode: %s" % vehicle.mode.name
# print " Is Armable?: %s" % vehicle.is_armable
# print " Armed: %s" % vehicle.armed
#
# print "Download the vehicle waypoints (commands). Wait until download is complete."
# cmds = vehicle.commands
# cmds.download()
# cmds.wait_ready()
#
# # Get the home location
# home_origin = vehicle.home_location
# print "Launch Home = " + str(home_origin)
#
# # Set Locations
# print "New Home" + str(TargetHomeGPS)
# home_hover = LocationGlobal(TargetHomeGPS[0], TargetHomeGPS[1], TargetHomeGPS[2])
# home_hover.alt = TargetHomeGPS[2] + 5
# home_ground = LocationGlobal(TargetHomeGPS[0], TargetHomeGPS[1], TargetHomeGPS[2])
# home_ground.alt = TargetHomeGPS[2] - 15   # Make this a number that is slightly below the ground
# time.sleep(1)
#
# # Change Home Location
# i = 0
# while str(home_origin) == str(vehicle.home_location):
#     i = i + 1
#     vehicle.home_location = home_ground
#     print "Updating home location Attempt #: " + str(i)
#     if i > 10:
#         print"Could not update new home location. Exiting"
#         vehicle.close()
#     time.sleep(1)
# print "Successfully updated home location"
#
# print "Traveling over New Home"
# vehicle.airspeed = TravelSpeed
# vehicle.groundspeed = TravelSpeed
# vehicle.simple_goto(home_hover)
# time.sleep(5)    # Increases for longer travel distances
#
# print "Landing"
# vehicle.airspeed = LandingSpeed
# vehicle.groundspeed = LandingSpeed
# vehicle.mode = VehicleMode("RTL")  # Go to home
# vehicle.armed = False
# vehicle.close()

MyIP = 'udpin:0.0.0.0:14550'     # Only works when on the right network.
vehicle = connect(MyIP, wait_ready=True)
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

home_origin = vehicle.home_location
home_ground = LocationGlobal(TargetHomeGPS[0], TargetHomeGPS[1], TargetHomeGPS[2])
home_ground.alt = TargetHomeGPS[2] - 5
time.sleep(1)
i=0
while str(home_origin) == str(vehicle.home_location):
    i = i + 1
    vehicle.home_location = home_ground
    print "Updating home location Attempt #: " + str(i)
    if i > 10:
        print"Could not update new home location. Exiting"
        vehicle.close()
    time.sleep(1)
print "Successfully updated home location"

vehicle.airspeed = 2
vehicle.groundspeed = 2
print "Go home"
vehicle.mode = VehicleMode("RTL")  # Go to home
time.sleep(5)
vehicle.mode = VehicleMode("RTL")  # Go to home
time.sleep(5)
vehicle.mode = VehicleMode("RTL")  # Go to home
time.sleep(5)
vehicle.mode = VehicleMode("RTL")  # Go to home
time.sleep(5)
vehicle.mode = VehicleMode("RTL")  # Go to home
time.sleep(5)
vehicle.armed = False
vehicle.close()