#!/usr/bin/env python3

from os import popen as _popen

f = open('all_in_one.sh', 'w')

def popen(what: str):
    # _popen(what)
    f.write(what + "\n")