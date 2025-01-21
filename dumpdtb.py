#!/usr/bin/python2

import argparse
from pyfdt.pyfdt import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dumb dtb')
    parser.add_argument('in_filename', help="input filename")
    args = parser.parse_args()
    with open(args.in_filename, 'rb') as infile:
        print FdtBlobParse(infile).to_fdt().to_dts()
