"""
TELEPYTHIC -- a python interface to test equipment
Copyright 2014 by Martijn Jasperse
https://bitbucket.org/martijnj/telepythic

Simple test script that forces scope to print to server.
Useful for debugging the print server code without having to physically press the button every time.
"""
import sys
from telepythic.library import TekScope

if __name__ == "__main__":
    ip = sys.argv[1]
    print 'Connecting to',ip
    dev = TekScope(sys.argv[1])
    print 'Printing to', dev.ask('HARDCopy:ACTIVe?')
    dev.write('HARDCopy')
