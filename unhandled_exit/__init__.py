import threading
import os
import sys

_orig_threading_excepthook = None
_orig_sys_excepthook = None
_active = False


def _threading_excepthook(args):
    _orig_threading_excepthook(args)
    print(f"{__name__}: exiting process due to unhandled exception in thread", file=sys.stderr, flush=True)
    os._exit(1)


def _sys_excepthook(type, value, traceback):
    _orig_sys_excepthook(type, value, traceback)
    print(f"{__name__}: exiting process due to unhandled exception in main", file=sys.stderr, flush=True)
    os._exit(1)


def activate():
    """
    `activate()` enables the functionality of the `unhandled_exit`
    package. After calling `activate()`, the whole process will
    exit if an unhandled exception occurs in a thread or in main.

    This works by chaining `os._exit(1)` after `threading.excepthook` and
    `sys.excepthook`.

    It is safe to call `activate()` multiple times.
    The second and later calls will be no-ops.
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
    `deactivate()` resets `threading.excepthook` and `sys.excepthook`
    to the values they had before `activate()`.

    It is safe to call `deactivate()` multiple times.
    The second and later calls will be no-ops.

    If `threading.excepthook` and/or `sys.excepthook` have been
    changed between `activate()` and `deactivate()`, a warning
    is printed and this excepthook is left as-is.
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
