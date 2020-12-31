#!/usr/bin/env python3

from subprocess import Popen, PIPE

commands = open('.all_in_one.sh', 'w')

def popen(what: str):
    commands.write(what + "\n")
    retcode = Popen(what, shell=True).wait()
    if retcode != 0:
        raise RuntimeError('command `%s` returned with error code %d' % (what, retcode))

def ask_if_continue(e: Exception):
    print(e)
    if input('An `%s` raised. Continue? Y/n' % e.__class__.__name__).strip().lower() == 'n':
        raise e