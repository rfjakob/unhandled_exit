#!/usr/bin/env python3
#
# Crash in a single-threaded application
#
# You can run this script without installing unhandled_exit using
# "hatch run":
#
#   hatch run tests/crash_single.py

import unhandled_exit
unhandled_exit.activate()

x = 1/0
