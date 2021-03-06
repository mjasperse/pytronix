from setuptools import setup
setup(
    name = "pytronix",
    version = "0.83",
    packages = [ 'pytronix' ],
    package_dir = { 'pytronix':'' },
    package_data = { '': ['LICENSE.txt','README.md'] },
    install_requires = [ 'telepythic' ],
    
    # metadata for upload to PyPI
    author = "Martijn Jasperse",
    author_email = "m.jasperse@gmail.com",
    description = "A python project to easily and rapidly download data from TekTronix DSOs",
    long_description = "This project provides the ability to quickly downloading scope data from a TekTronix digital oscilloscope using the telnet interface.",
    license = "BSD",
    keywords = "TekTronix TDS DPO MSO CRO scope HDF5",
    url = "https://github.com/mjasperse/pytronix",

    # could also include long_description, download_url, classifiers, etc.
)
