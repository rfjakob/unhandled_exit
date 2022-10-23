# The tests are based on the fact that unhandled_exit
# should exit with code 1 and the tested scripts go into
# and endless loop otherwise.
#
# If unhandled_exit for some reason does not exit the process,
# "timeout" kills it after and returns code 124.
# This is verfied in test_nocrash().

import os


def test_crash_main():
    ret = os.system("timeout -v 10 ./tests/crash_main.py") >> 8
    assert ret == 1


def test_crash_thread():
    ret = os.system("timeout -v 10 ./tests/crash_thread.py") >> 8
    assert ret == 1


def test_crash_single():
    ret = os.system("timeout -v 10 ./tests/crash_single.py") >> 8
    assert ret == 1


def test_nocrash():
    ret = os.system("timeout -v 0.1 ./tests/nocrash.py") >> 8
    assert ret == 124
