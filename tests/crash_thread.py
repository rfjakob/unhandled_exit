#!/usr/bin/env python3

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
