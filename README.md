# parse-xrd
Parses .uxd-files from a 2theta-omega scan from a Bruker D8 XRD system.


## Usage

Use from a command line prompt as

    $ parse-xrd.py <input_file.uxd>

This creates a output file `<input_file-out.csv>` in the format

    2theta,counts
    39.2,10
    39.3,13
    39.4,15

with all the (2theta,counts)-values in the file.

It is also possible to use a wildcard to parse all valid files in a given directory,
e.g.

    $ parse-xrd.py *.uxd

which again will create output files with individual names.

For ease of use, add the folder destination to your $PATH, so you can use it
in any directory.

