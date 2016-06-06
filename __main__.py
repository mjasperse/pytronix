"""
TELEPYTHIC -- a python interface to test equipment
Copyright 2014 by Martijn Jasperse
https://bitbucket.org/martijnj/telepythic

Module file to provide convenience interface. Call with
$ python -m pytronix [options]
where valid options are described by -h.
"""
import pytronix
import telepythic
import argparse
from configure import configure_scope

parser = argparse.ArgumentParser(
	description='''scrape data from TekTronix digital oscilloscopes either using a network connection, or through VISA.
		Data is saved to a timestamped H5 file in the current directory.'''
)
group = parser.add_mutually_exclusive_group()
group.add_argument('-s', nargs='?', metavar='port', type=int, help='start pytronix server (on specified port).')
group.add_argument('--ip', '-i', metavar='host', help='connect to scope with specified hostname.')
group.add_argument('--usb', '-u', action='store_true', help='connect to scope over USB.')
group.add_argument('--visa', '-V', metavar='dev', help='connect to specified VISA device')
parser.add_argument('--timeout', '-t', metavar='t0', default=3, help='communications timeout (in seconds)')
parser.add_argument('--configure', '-C', action='store_true', help='configure device for use with print server')
args = parser.parse_args()

instr = None
if args.usb:
	# try to find an attached USB device
	instr = telepythic.pyvisa_connect('USB?*::INSTR',timeout=args.timeout)
elif args.visa is not None:
	# explicitly connect to the specified VISA connection
	instr = telepythic.pyvisa_connect(args.visa,timeout=args.timeout)
elif args.ip is not None:
	# use a telnet connection to specified IP
	instr = args.ip

if instr is None:
	# no argument means start the "print" server
	pytronix.serve()
elif args.configure:
    # should we try to configure the instrument?
    configure_scope(instr)
else:
    # not doing configure, so perform a data scrape
    pytronix.scrape(instr)
