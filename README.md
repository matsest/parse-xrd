# parse_xrd.py
Parses .uxd-files from a 2theta-omega scan from a Bruker D8 XRD system.


## Usage

Use from a command line prompt as

    $ parse_xrd.py <input_file.uxd>

This creates a output file `<input_file-out.csv>` in the format

    2theta,counts
    39.2,10
    39.3,13
    39.4,15

with all the (2theta,counts)-values in the file.