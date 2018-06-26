import os
import subprocess
import argparse
import exceptions

parser = argparse.ArgumentParser(description='retrieve MAC adress of targeted network adapter')
parser.add_argument('--verbose','-v', action='store_true', required=False,
                    help='Enable Verbose mode')
parser.add_argument('--adapter', '-a', required=True,
                    help='Sets new coordinates for Drone to land at. Enter coordinates as 3 separate objects')

args = parser.parse_args()


def verbose(string):
    try:
        if args.verbose:
            print string
    except IOError as err:
        print err


verbose("Adapter = " + args.adapter)

ifconfig = os.popen("ifconfig").read()
verbose(ifconfig)

split = ifconfig.split()
i = split.index(args.adapter + ":")
split = split[i + 1:]
i = split.index("ether")
split = split[i + 1:]

MAC = split[0]
print MAC
