"""Modules, import styles, and the local helpers package."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Modules and Imports")
    print("2: Packages and __init__.py")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Modules and Imports
        # ==================================================
        print("--> Modules and Imports")

        # A module is a Python file. Importing it gives access to its names.
        # helpers/math_helpers.py is a module inside the helpers package.
        import helpers.math_helpers

        result = helpers.math_helpers.add_numbers(10, 5)
        print(f"module import: {result}")

        # Import one function to use its name without the module prefix.
        from helpers.math_helpers import add_numbers

        result = add_numbers(20, 5)
        print(f"function import: {result}")

        # Import multiple names from the same module.
        from helpers.math_helpers import add_numbers, multiply_numbers

        print(f"multiple imports - sum: {add_numbers(10, 5)}")
        print(f"multiple imports - product: {multiply_numbers(10, 5)}")

        # Aliases provide an alternative local name for a module or function.
        import helpers.math_helpers as mh
        from helpers.math_helpers import multiply_numbers as multiply

        print(f"module alias: {mh.add_numbers(10, 5)}")
        print(f"function alias: {multiply(10, 5)}")

        # The standard library ships with Python; no pip install is needed.
        from datetime import datetime

        print(f"current time: {datetime.now()}")
        # Imports are placed beside each example to show the different forms.
        # In a typical application, group imports at the top of the file.

    elif selection == "2":
        # ==================================================
        # Packages and __init__.py
        # ==================================================
        print("--> Packages and __init__.py")

        # A regular package groups modules in a directory with __init__.py.
        import helpers
        from helpers import math_helpers

        print(f"package file: {helpers.__file__}")
        print(f"module file: {math_helpers.__file__}")
        print(f"sum from package module: {math_helpers.add_numbers(10, 5)}")

        # Importing helpers runs helpers/__init__.py once on the first import.
        # Ours documents the package without running examples or re-exporting names.
        # Import the functions from their module explicitly when needed.
        from helpers.math_helpers import add_numbers

        print(f"direct function import: {add_numbers(20, 5)}")
        # src contains runnable scripts; it does not need an __init__.py.

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
