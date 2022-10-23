# unhandled_exit

[![CI](https://github.com/rfjakob/unhandled_exit/actions/workflows/ci.yml/badge.svg)](https://github.com/rfjakob/unhandled_exit/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/unhandled_exit.svg)](https://pypi.org/project/unhandled_exit/)

*unhandled_exit* makes the whole process exit if an unhandled
exception occours in a thread or in main.

Uses [`threading.excepthook`](https://docs.python.org/3/library/threading.html#threading.excepthook)
which is only available in Python 3.8 and later. The
[automated tests](https://github.com/rfjakob/unhandled_exit/actions/workflows/ci.yml)
test Python 3.8, 3.9 and 3.10.

## Usage

```
import unhandled_exit
unhandled_exit.activate()
```

## Why

When using Python with threads, an uncaught exception no longer
exits the process, but only exits the affected thread.

This can make perfect sense if the application restarts threads
as needed, or the threads are disposable.

But if the application does not handle a thread exit, the application
can be left running in defunct state.

In this situation I (and some [1] other [2] people) [3]) find it preferable
to have the whole process exit with a bang so the service manager can
restart it and/or the developer can investigate what went wrong.

## API Documentation

### activate()

`activate()` enables the functionality of the *unhandled_exit*
package. After calling `activate()`, the whole process will
exit if an unhandled exception occurs in a thread or in main.

This works by chaining `os._exit(1)` after `threading.excepthook` and
`sys.excepthook`.

It is safe to call `activate()` multiple times.
The second and later calls will be no-ops.

### deactivate()

`deactivate()` resets `threading.excepthook` and `sys.excepthook`
to the values they had before `activate()`.

It is safe to call `deactivate()` multiple times.
The second and later calls will be no-ops.

If `threading.excepthook` and/or `sys.excepthook` have been
changed between `activate()` and `deactivate()`, a warning
is printed and this excepthook is left as-is.

## Development

Get the code:

```
git clone https://github.com/rfjakob/unhandled_exit
cd unhandled_exit
```

Run the Test Suite (needs `pip install hatch`):

```
make test
```

Output should look like this:
```
python -m compileall -q .
hatch run test
========================== test session starts ===========================
platform linux -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0 -- /home/jakob/.local/share/hatch/env/virtual/unhandled-exit/PB23ljro/unhandled-exit/bin/python
cachedir: .pytest_cache
rootdir: /home/jakob.donotbackup/code/unhandled_exit
plugins: cov-4.0.0
collected 4 items                                                        

tests/tests.py::test_crash_main PASSED                             [ 25%]
tests/tests.py::test_crash_thread PASSED                           [ 50%]
tests/tests.py::test_crash_single PASSED                           [ 75%]
tests/tests.py::test_nocrash PASSED                                [100%]

=========================== 4 passed in 0.18s ============================
```

Publish to pypi (needs `pip install hatch`):

```
make publish
```

## References

[1] https://stackoverflow.com/questions/49663124/cause-python-to-exit-if-any-thread-has-an-exception

[2] https://stackoverflow.com/questions/57208345/how-to-kill-process-if-thread-encounters-exception

[3] https://stackoverflow.com/questions/71051325/is-there-any-way-to-stop-all-workers-in-a-threadpool-if-any-of-the-worker-raise
