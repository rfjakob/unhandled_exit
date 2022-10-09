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

# Hacking

Many commands here require `hatch` (`pip install hatch`).

## Run the Test Suite

```
hatch run test
```

## Publish to pypi

```
hatch publish
```
