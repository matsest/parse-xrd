#! /usr/bin/env python

import csv
import sys
import os

def read_xrd_data(datafile):
    """Reads a uxd-datafile <datafile> and outputs two lists: two_theta,intensity"""

    with open(datafile, 'r') as my_file:

        x = []
        y = []

        reader = csv.reader(my_file, delimiter=' ', skipinitialspace=True)

        for row in reader:
            if len(row) == 2:
                try:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
                except:
                    pass

    return x, y

def write_xrd_data(output_file, two_theta, intensity):
    """Writes to a csv-file <output_file> from two lists <two_theta>, <intensity>"""

    with open(output_file, 'w') as out:

        out_writer = csv.writer(out, delimiter=",")
        out_writer.writerow(["2theta", "counts"])

        for degree, count in zip(two_theta, intensity):
            out_writer.writerow([degree, count])

def count_rows(csv_file):
    """Counts number of rows in <csv_file>"""

    with open(csv_file, "r") as my_file:
        reader = csv.reader(my_file, delimiter=",")
        data = list(reader)
        return len(data)

def main():
    try:
        input_file = sys.argv[1]

        if not input_file.lower().endswith(".uxd"):
            print "Invalid file format. Use .uxd-files!"
            sys.exit(1)

        output_file = os.path.splitext(os.path.basename(input_file))[0] + "-out.csv"

    except IndexError:
        print "No input file given!"
        sys.exit(1)

    try:
        two_theta, intensity = read_xrd_data(input_file)
        write_xrd_data(output_file, two_theta, intensity)

        print "XRD data printed sucessfully!"
        print "From: ", input_file
        print "To: ", output_file
        print "Datapoints: ", count_rows(output_file)

    except:
        print "Something went wrong. Invalid input file?"
        sys.exit(1)

if __name__ == "__main__":
    main()
