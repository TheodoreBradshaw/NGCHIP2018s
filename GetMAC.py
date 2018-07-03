import os
import argparse

parser = argparse.ArgumentParser(description='retrieve MAC address of targeted network adapter')
parser.add_argument('--verbose','-v', action='store_true', required=False,
                    help='Enable Verbose mode')
parser.add_argument('--adapter', '-a', required=True,
                    help="This argument identifies the adapter whose MAC will be returned")
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
