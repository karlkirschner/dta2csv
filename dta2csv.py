#!/usr/bin/env python3

# World Bank's DTA data conversion to csv file
# Author: Karl Kirschner, 2019

import argparse
import os
import pandas as pd


def convert_data(basename=None):

    try:
        os.path.exists('{0}.dta'.format(basename))
        print()
        print('Converting {0}.dta to {0}.csv.'.format(basename))
    except FileNotFoundError:
        print()
        print('The file ({0}.dta) does not exist.'.format(basename))

    data = pd.io.stata.read_stata('{0}.dta'.format(basename))
    data.to_csv('{0}.csv'.format(basename))


if __name__ == "__main__":
    """
    Usage: dta2csv.py -f input_file_name (without the .dta extension)
    
    Example for converting data.dta to data.csv: ./dta2csv.py -f data
    
    Note that this will overwrite an existing csv file.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--inputfile", type=str, help="Basename for DTA input data file.", action="store")
    args = parser.parse_args()
    convert_data(basename=args.inputfile)
