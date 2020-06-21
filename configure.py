"""
PYTRONIX
Copyright 2014-2020 by Martijn Jasperse
https://github.com/mjasperse/pytronix

Configure a TekTronix scope to set the active printer to THIS computer,
so that pressing the "print" button will start a scrape download
"""
import sys, time, socket
from telepythic.library import TekScope

def configure_scope(dev):
    # whoami? (existential like, woah)
    myip = dev.dev.sock.getsockname()[0]
    myname = socket.gethostname()
    print 'I am', myname, '=', myip
    
    # what printers are currently set up?
    printers = dev.ask('HARDCopy:PRINT:LIST?')
    print 'Printers:', printers
    # are we already on that list?
    namestr = ':'+myname+':Net::'
    i = printers.find(namestr)
    if i > 0:
        theip = printers[i+len(namestr):].split(';',1)[0]
        if myip != theip:
            print 'Found host match with incorrect IP',theip
            dev.write('HARDCopy:PRINT:DELete "%s"'%myname)
            i = -1
        else:
            print 'Found correct host match'
    else:
        print 'Not on printers list'
    # add this host as a printer
    if i < 0:
        print 'Adding to printers list'
        dev.write('HARDCopy:PRINTer:ADD "%s","","%s"'%(myname,myip))
    print 'Making active printer'
    # make this host the default printer
    dev.write('HARDCopy:ACTIVe "%s"'%myname)
    
    # set date and time while we're connected
    dev.write('DATE "%s"'%time.strftime('%Y-%m-%d'))
    dev.write('TIME "%s"'%time.strftime('%H:%M:%S'))


if __name__ == "__main__":
    # invoked as a script
    ip = sys.argv[1]
    print 'Connecting to',ip
    dev = TekScope(ip)
    configure_scope(dev)
    