import threading
import os
import sys

_orig_threading_excepthook = None
_orig_sys_excepthook = None
_active = False


def _threading_excepthook(args):
    _orig_threading_excepthook(args)
    print(f"{__name__}: exiting process due to unhandled exception in thread", file=sys.stderr)
    os._exit(1)


def _sys_excepthook(type, value, traceback):
    _orig_sys_excepthook(type, value, traceback)
    print(f"{__name__}: exiting process due to unhandled exception in main", file=sys.stderr)
    os._exit(1)


def activate():
    """
    Activate unhandled_exit and make the whole process exit if an unhandled
    exception occours in a thread or in main.

    This modifies `threading.excepthook` and `sys.excepthook`.
    """

    global _active
    if _active:
        return

    global _orig_threading_excepthook
    _orig_threading_excepthook = threading.excepthook
    threading.excepthook = _threading_excepthook

    global _orig_sys_excepthook
    _orig_sys_excepthook = sys.excepthook
    sys.excepthook = _sys_excepthook

    _active = True


def deactivate():
    """
    Deactivate unhandled_exit and restore the original behavoir when an
    unhandled exception occours.

    This resets `threading.excepthook` and `sys.excepthook` to their original
    values.
    """

    global _active
    if not _active:
        return

    if threading.excepthook == _threading_excepthook:
        threading.excepthook = _orig_threading_excepthook
    else:
        print(f"{__name__}: threading.excepthook was changed behind our back, keeping as-is", file=sys.stderr)

    if sys.excepthook == _sys_excepthook:
        sys.excepthook = _orig_sys_excepthook
    else:
        print(
            f"{__name__}: sys.excepthook was changed behind our back, keeping as-is", file=sys.stderr)

    _active = False
