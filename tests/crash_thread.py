#!/usr/bin/env python3
#
# Crash in background thread
#
# You can run this script without installing unhandled_exit using
# "hatch run":
#
#   hatch run tests/crash_thread.py

import threading
import time
import sys

import unhandled_exit
unhandled_exit.activate()


def t1_func():
    x = 1/0


threading.Thread(target=t1_func).start()

while True:
    time.sleep(1)
    print("main thread still here", file=sys.stderr)
