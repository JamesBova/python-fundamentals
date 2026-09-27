"""Python environments and pip commands for Windows; commands are reference text."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Python Interpreter")
    print("2: Virtual Environments")
    print("3: pip and Dependencies")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Python Interpreter
        # ==================================================
        print("--> Python Interpreter")

        import sys

        # These values describe the interpreter actually running this script.
        print(f"Python version: {sys.version}")
        print(f"Interpreter path: {sys.executable}")
        print("Windows commands to inspect Python:")
        print("  py --version")
        print("  python --version")
        print("  where.exe python")
        # PowerShell uses where as an alias; where.exe calls the Windows tool.

    elif selection == "2":
        # ==================================================
        # Virtual Environments
        # ==================================================
        print("--> Virtual Environments")

        # A virtual environment isolates installed packages for one project.
        # These commands are printed for reference, not executed by this lesson.
        print(r"Run from the repository root in PowerShell:")
        print(r"  py -m venv .venv")
        print(r"  .\.venv\Scripts\Activate.ps1")
        print(r"  python --version")
        print(r"  deactivate")
        print(r"Command Prompt activation: .venv\Scripts\activate.bat")
        print(r"Without activation: .\.venv\Scripts\python.exe src\basics.py")
        print("Keep .venv/ in .gitignore; recreate environments instead of committing them.")

    elif selection == "3":
        # ==================================================
        # pip and Dependencies
        # ==================================================
        print("--> pip and Dependencies")

        # python -m pip uses pip belonging to the selected Python interpreter.
        # General installation pattern: python -m pip install package_name
        print("Inspect installed packages: python -m pip list")
        print("Install project dependencies: python -m pip install -r requirements.txt")
        print("This project currently uses only Python's standard library.")
        print("Optional installation example: python -m pip install requests")
        print("requests is a third-party package; it is not needed for these lessons.")
        print("Remove that optional package: python -m pip uninstall requests")
        print("Environment snapshot: python -m pip freeze")
        # To save a snapshot: python -m pip freeze > requirements.txt
        # freeze lists installed packages, including dependencies and experiments.
        # Review that output before copying anything into requirements.txt.
        print("Keep requirements.txt limited to packages the project actually needs.")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
