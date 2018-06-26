#!/usr/bin/python
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
import sys
import argparse

parser = argparse.ArgumentParser(description='Take control of drone and land at given GPS coordinates')
parser.add_argument('--debug', '-d', action='store_true', required=False,
                    help='Enable Debug mode and should stop the drone from flying')
parser.add_argument('--verbose','-v', action='store_true', required=False,
                    help='Enable Verbose mode')
parser.add_argument('--gps', '-g', nargs=3, type=float,
                    help='Sets new coordinates for Drone to land at. Enter coordinates as 3 separate objects')

args = parser.parse_args()


def verbose(string):
    if args.verbose:
        print string


verbose(args.debug)
verbose(args.gps)


def MoveTo(latitude, longitude, altitude):
    print "Hello World!?!"

    # # Vars
    # MyIP = 'udpin:0.0.0.0:14550'     # Only works when on the right network.
    # # TargetHomeGPS = [39.3031664, -84.4779333, 223]    # Hardcoded GPS Coordinate, this should be the input variable
    # # TargetHomeGPS = [39.302870, -84.477827, 233]      # Far downfield, backup coordinates.
    #
    # TravelSpeed = 3   # integer, speed in m/s, Matt = [3, 5]
    # LandingSpeed = 1    # integer, speed in m/s, Matt = 3
    #
    # # Connect
    # print MyIP
    # vehicle = connect(MyIP, wait_ready=True)
    # vehicle.mode = VehicleMode("GUIDED")
    # vehicle.armed = True
    #
    # print "Downloading the vehicle waypoints (commands). Wait until download is complete."
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
    # home_hover.alt = TargetHomeGPS[2] + 20
    # home_ground = LocationGlobal(TargetHomeGPS[0], TargetHomeGPS[1], TargetHomeGPS[2])
    # home_ground.alt = TargetHomeGPS[2] - 5   # Make this a number that is slightly below the ground
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

    # Simple Version
    MyIP = 'udpin:0.0.0.0:14550'     # Only works when on the right network.
    vehicle = connect(MyIP, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")
    if args.debug:
        vehicle.armed = False
    else:
        vehicle.armed = True

    home_origin = vehicle.home_location
    home_ground = LocationGlobal(latitude, longitude, altitude)
    home_ground.alt = altitude - 10
    time.sleep(1)

    i = 0
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


# if not args.debug:
    MoveTo(args.gps[0], args.gps[1], args.gps[2])