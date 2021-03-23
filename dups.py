#!/usr/bin/env python3

import sys
import re

duplicates = 0

if len(sys.argv) < 2:
    print("usage: dups <file> ...\n")

lastword = ""
linenum = 0

for fname in sys.argv[1:]:
    for line in open(fname, 'r'):
        linenum += 1
        words = re.split(r'\W+', line)

        for word in words:
            if re.match(r'^\s*$', word):
                continue

            if re.match(r'^\W+$', word):
                lastword = ""
                continue

            if word.lower() == lastword.lower():
                print(f"{fname}:{linenum} {word}")
                duplicates += 1

            lastword = word

    print(duplicates)
