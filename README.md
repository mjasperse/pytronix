# Pytronix - One button trace extraction#

This project provides the ability to quickly downloading scope data from a TekTronix digital oscilloscope using the telnet interface.

There are script files that provide the functionality to scrape raw waveform data to an HDF5 file either by using the machine's name or IP address, or to set up a print server which then downloads the data automatically when you press the "print" button on the DSO.

All currently visible channels are downloaded, and all waveform settings are stored in the HDF5 file with the scope data. Direct binary transfer mode is used to make acquisition quick, and files are saved with the timestamp of when the transfer was initiated. If a "print" is initiated from the DSO, the resulting postscript file that the DSO generates is also saved.

**Using pytronix provides a convenient "one click" way to save data from a TekTronix DSO for later analysis.**

Uses the [telepythic library](https://bitbucket.org/martijnj/telepythic) for handling underlying communications.


### How do I use it? ###
Pytronix is most easily executed from the command line as a python module.
Install from the cheeseshop with `pip install pytronix` and then invoke with
```
python -m pytronix [options]
```

Invoking without options (or with `-s`) starts the print server,
```
python -m pythonix
```
To download all visible traces from the scope at 192.168.1.10,
```
python -m pytronix -i 192.168.1.10
```
To configure that scope to print to this machine whenever the "hard copy" button is pressed,
```
python -m pytronix -i 192.168.1.10 -C
```
Alternatively, to download data from a scope connected over USB,
```
python -m pytronix -u
```

The scripts `pytronix.py` and `configure.py` can also be executed from the commandline directly.
