#!/usr/bin/env python3
#
# Infinite loop, no crash

import time
import sys

while True:
    time.sleep(1)
    print("main thread still here", file=sys.stderr)
