#!/usr/bin/python
from dronekit import connect, VehicleMode, LocationGlobal
import time
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


def delta(attribute):
    a = attribute
    time.sleep(1)
    b = attribute
    c = int(b - a)
    return c


def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # send command to vehicle on 1 Hz cycle
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)


verbose(args.debug)
verbose(args.gps)


def MoveTo(latitude, longitude, altitude):
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
    MyIP = 'udpin:0.0.0.0:14550'
    vehicle = connect(MyIP, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")

    while str(vehicle.mode) == str(VehicleMode("GUIDED")):
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
            verbose("Updating home location Attempt #: " + str(i))
            if i > 10:
                verbose("Could not update new home location. Exiting")
                vehicle.close()
            time.sleep(1)
        verbose("Successfully updated home location")

        vehicle.airspeed = 2
        vehicle.groundspeed = 2
        verbose("Go home")

        vehicle.mode = VehicleMode("RTL")

        while True:
            if delta(vehicle.altitude) > 0:
                up = True
                if level or down:
                    send_ned_velocity(0,0,5,1)
            elif delta(vehicle.altitude) < 0:
                down = True
                pass
            else:
                level = True
                if down:
                    print vehicle.capabilities.flight_termination
                    vehicle.capabilities.flight_termination = True
                    vehicle.armed = False

            time.sleep(1)
            if not vehicle.armed:
                vehicle.close()
                print "Vehicle Landed successfully"
                exit()

    while vehicle.mode != VehicleMode("GUIDED"):
        verbose("Controller Override, attempting to reconnect...")
        vehicle.close()
        MoveTo(args.gps[0], args.gps[1], args.gps[2])


# if not args.debug:


MoveTo(args.gps[0], args.gps[1], args.gps[2])
