# The tests are based on the fact that unhandled_exit
# should exit with code 1 and the tested scripts go into
# and endless loop otherwise.
#
# If unhandled_exit for some reason does not exit the process,
# "timeout" kills it after and returns code 124.
# This is verfied in test_nocrash().

import subprocess


def verify_ret(ret):
    """
Output should look like this:

$ hatch run tests/crash_main.py

Traceback (most recent call last):
  File "/home/jakob.donotbackup/code/unhandled_exit/tests/crash_main.py", line 26, in <module>
    x = 1/0
ZeroDivisionError: division by zero
unhandled_exit: exiting process due to unhandled exception in main

exit code 1
    """
    assert ret.returncode == 1
    stderr = ret.stderr.decode("utf8", "ignore")
    assert "Traceback" in stderr
    assert "unhandled_exit" in stderr
    assert not ret.stdout


def test_crash_main():
    ret = subprocess.run("timeout -v 10 ./tests/crash_main.py",
                         shell=True, capture_output=True)
    verify_ret(ret)


def test_crash_thread():
    ret = subprocess.run(
        "timeout -v 10 ./tests/crash_thread.py", shell=True, capture_output=True)
    verify_ret(ret)


def test_crash_single():
    ret = subprocess.run(
        "timeout -v 10 ./tests/crash_single.py", shell=True, capture_output=True)
    verify_ret(ret)


def test_nocrash():
    ret = subprocess.run("timeout -v 0.1 ./tests/nocrash.py",
                         shell=True, capture_output=True)
    assert ret.returncode == 124
