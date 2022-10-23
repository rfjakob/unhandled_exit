#!/usr/bin/env python3
#
# Crash in main thread with a background thread running
#
# You can run this script without installing unhandled_exit using
# "hatch run":
#
#   hatch run tests/crash_main.py

import threading
import time
import sys

import unhandled_exit
unhandled_exit.activate()


def t1_func():
    while True:
        time.sleep(1)
        print("background thread still here", file=sys.stderr)


threading.Thread(target=t1_func).start()

x = 1/0
