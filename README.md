# Python Fundamentals

A personal Python reference and demonstration of the concepts learned in the
completed instructional portion of Python Fundamentals. The files break down
individual concepts with readable, runnable examples, rather than forming an
application. Examples intentionally show several ways to apply a concept.
An integrated Python Fundamentals mini-project will be
added next; it has not been implemented yet.

## Topics and project structure

```text
Python-Fundamentals/
├── README.md
├── .gitignore
├── requirements.txt          # No third-party dependencies currently required
├── src/
│   ├── main.py               # Prints directions for using the reference
│   ├── basics.py             # Variables, types, strings, numbers, Booleans
│   ├── collections_demo.py   # Lists, tuples, sets, dictionaries
│   ├── control_flow.py       # if/elif/else, for/while, break, continue
│   ├── functions.py          # Definitions, arguments, returns, scope, hints
│   ├── comprehensions.py     # List/dictionary creation, transformations, filtering
│   ├── error_handling.py     # try/except/else/finally, exception types, raise
│   ├── organization.py       # Modules, import forms, aliases, packages
│   ├── classes_demo.py       # Classes, instances, attributes, self, methods
│   ├── environment.py        # Interpreter, virtual environments, pip, dependencies
│   └── helpers/
│       ├── __init__.py       # Documents the regular package
│       └── math_helpers.py   # Reusable arithmetic functions for import examples
└── tests/                    # Reserved empty folder; no test suite yet
```

`src` contains runnable scripts and is not a package. `helpers` is a package;
its `__init__.py` has no example output or automatic function exports.
The classes lesson progresses from class → object/instance → attributes →
`self` → `__init__` → methods → class versus instance attributes.
The functions lesson includes positional and keyword arguments, default arguments,
local and global scope, and basic type hints.

## Windows environment setup

Use Python 3.9 or newer (the examples use `list[str]` type hints). Run these
commands from the repository root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -m pip install -r requirements.txt
```

If `py` is unavailable but Python is on your PATH, use `python -m venv .venv`.
In Command Prompt, activate with `.venv\Scripts\activate.bat` instead.
Use `deactivate` when finished.

If PowerShell blocks the activation script, you can use the environment directly
without changing your execution policy:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\basics.py
```

The examples require only the standard library and local modules, so installing
the current `requirements.txt` adds no packages. The optional `requests`
installation shown in `environment.py` is for learning pip, not a project
dependency. Keep `.venv/` out of Git; it is already excluded in `.gitignore`.

## Run the learning examples

With the environment activated, choose any topic:

```powershell
python src/basics.py
python src/collections_demo.py
python src/control_flow.py
python src/functions.py
python src/comprehensions.py
python src/error_handling.py
python src/organization.py
python src/classes_demo.py
python src/environment.py
```

Each topic uses the same menu: enter a section number to run that section, or
`0` to exit. Invalid input prints a message without a traceback. Each run executes
one section; run the file again to choose another. The while-loop section asks for
the practice password `python` and keeps asking until it matches.

`python src/main.py` prints orientation only. Each topic is readable on its own;
the import lesson uses `helpers/math_helpers.py`. The
`if __name__ == "__main__":` guard prevents menus and examples from running on
import. It does not create a function scope, so the global-scope examples remain
accurate. The lesson files are references, not libraries of reusable functions.

Deliberately failing examples in `error_handling.py` catch their expected errors.
Examples of invalid tuple/set operations remain commented out. Set display order,
object representations, interpreter paths, and the current time can vary by run.
The environment lesson prints setup commands for reference; it does not install
packages or change your environment.
