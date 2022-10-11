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
