#!/usr/bin/env python3

import os
import platform

assert(os.name == 'posix')
assert(platform.system() == 'Darwin')

version, _, arch = platform.mac_ver()

assert(tuple([int(c) for c in version.split('.')]) >= (10, 13, 0))
assert(arch in ['x86_64', 'arm64'])