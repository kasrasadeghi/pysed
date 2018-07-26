#!/usr/local/bin/python3
""" support full regular expressions"""
import re
import sys
_, pattern, replacement, *files = sys.argv

for filename in files:
    print(filename)
    with open(filename, "r") as f:
        c = f.read()
        c = re.sub(pattern, replacement, c)
    with open(filename, "w") as f:
        f.write(c)
