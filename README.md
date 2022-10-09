# unhandled_exit

unhandled_exit makes the whole process exit if an unhandled
exception occours in a thread or in main.

Uses [`threading.excepthook`](https://docs.python.org/3/library/threading.html#threading.excepthook)
which is only available in Python 3.8 and later.

## Usage

```
import unhandled_exit
unhandled_exit.activate()
```

## Examples

[crash_main.py](https://github.com/rfjakob/unhandled_exit/blob/master/tests/crash_main.py)
[crash_thread.py](https://github.com/rfjakob/unhandled_exit/blob/master/tests/crash_thread.py)

# Hacking

Get the code:

```
git clone https://github.com/rfjakob/unhandled_exit
cd unhandled_exit
```

Run the Test Suite:

```
hatch run test
```

Publish to pypi:

```
hatch clean
hatch build
hatch publish
```
