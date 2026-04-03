#!/usr/bin/env python

# repairs a corrupted /$RECYCLE.BIN/'s R-files (data) and I-files (metadata)

import struct

def parse_I_file(path):
    with open(path, 'rb') as f:
        data = f.read()

    # Skip header (first 24 bytes usually)
    name = data[24:].decode('utf-16le', errors='ignore').rstrip('\x00')
    return name

# ex: print(parse_I_file("I1A2B3C.jpg"))