#!/usr/bin/env python3

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
