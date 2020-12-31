#!/usr/bin/env python3

from subprocess import Popen, PIPE

commands = open('.all_in_one.sh', 'w')

def popen(what: str):
    commands.write(what + "\n")
    assert(Popen(what, shell=True).wait() == 0)

def ask_if_continue(e: Exception):
    if input('continue? Y/n').strip().lower() == 'n':
        raise e