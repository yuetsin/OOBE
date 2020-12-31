#!/usr/bin/env python3

from os import popen

def _update_brew():
    popen('brew update')