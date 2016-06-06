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

parser = argparse.ArgumentParser(
	description='''scrape data from TekTronix digital oscilloscopes either using a network connection, or through VISA.
		Data is saved to a timestamped H5 file in the current directory.'''
)
group = parser.add_mutually_exclusive_group()
group.add_argument('-s', nargs='?', metavar='port', type=int, help='start pytronix server (on specified port).')
group.add_argument('--ip', '-i', nargs=1, metavar='host', help='connect to scope with specified hostname.')
group.add_argument('--usb', '-u', action='store_true', help='connect to scope over USB.')
group.add_argument('--visa', '-V', nargs=1, metavar='dev', help='connect to specified VISA device')
args = parser.parse_args()

if args.usb:
	# try to find an attached USB device
	instr = telepythic.pyvisa_connect('USB?*::INSTR',timeout=2)
	pytronix.scrape(instr)
elif args.visa is not None:
	# explicitly connect to the specified VISA connection
	instr = telepythic.pyvisa_connect(args.visa[0],timeout=2)
	pytronix.scrape(instr)
elif args.ip is not None:
	# use a telnet connection to specified IP
	pytronix.scrape(args.ip[0])
else:
	# no argument means start the "print" server
	pytronix.serve()
