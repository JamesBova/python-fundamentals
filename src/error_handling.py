"""Handle specific exceptions and raise validation errors."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Basic Exception Handling")
    print("2: Exception Types")
    print("3: Raising Exceptions")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Basic Exception Handling
        # ==================================================
        print("--> Basic Exception Handling")

        # Handle an error using try and except
        try:
            number = int("Bob")
            print(f"number: {number}")
        except ValueError:
            print("Could not convert value to an integer.")

        # Successful try block
        try:
            number = int("25")
            print(f"converted number: {number}")
        except ValueError:
            print("Could not convert value to an integer.")

        # Code after the error inside the try block is skipped
        try:
            print("Starting conversion.")
            number = int("Bob")
            print("Conversion finished.")
        except ValueError:
            print("Conversion failed.")

        # finally runs whether the try succeeds or fails
        try:
            number = int("Bob")
            print(f"number: {number}")
        except ValueError:
            print("Conversion failed.")
        finally:
            print("Conversion attempt finished.")

    elif selection == "2":
        # ==================================================
        # Exception Types
        # ==================================================
        print("--> Exception Types")

        # ValueError
        try:
            number = int("Bob")
        except ValueError:
            print("ValueError: invalid number.")

        # ZeroDivisionError
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("ZeroDivisionError: cannot divide by zero.")

        # IndexError
        try:
            names = ["Bob", "Alice"]
            print(names[5])
        except IndexError:
            print("IndexError: list index does not exist.")

        # KeyError
        try:
            person = {
                "name": "Bob",
                "age": 20
            }
            print(person["city"])
        except KeyError:
            print("KeyError: dictionary key does not exist.")

        # Handle different exception types separately
        try:
            value = "0"
            number = int(value)
            result = 100 / number
        except ValueError:
            print("ValueError: value must be a number.")
        except ZeroDivisionError:
            print("ZeroDivisionError: cannot divide by zero.")

        # Access the exception object
        try:
            number = int("Bob")
        except ValueError as error:
            print(f"Error message: {error}")

        # Catch specific exceptions first. A broad fallback is shown for reference.
        # Prefer specific handlers when you know which errors to expect.
        try:
            number = int("Bob")
        except ValueError:
            print("Known ValueError occurred.")
        except Exception as error:
            print(f"Unexpected error: {error}")

        try:
            number = int("25")
        except ValueError:
            print("Invalid number.")
        else:  # Runs only when the try block succeeds.
            print(f"Conversion succeeded: {number}")

    elif selection == "3":
        # ==================================================
        # Raising Exceptions
        # ==================================================
        print("--> Raising Exceptions")

        # Raise an exception manually
        def validate_age(age):
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return True

        try:
            validate_age(-5)
        except ValueError as error:
            print(f"Validation error: {error}")

        # Raise an exception based on business rules
        def calculate_price(quantity):
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            return quantity * 10

        try:
            price = calculate_price(5)
            print(f"price: {price}")
        except ValueError as error:
            print(f"Error: {error}")

        # Data validation example
        def validate_transaction(amount):
            if amount < 0:
                raise ValueError("Transaction amount cannot be negative.")
            if amount == 0:
                raise ValueError("Transaction amount cannot be zero.")
            return True

        try:
            validate_transaction(-50)
        except ValueError as error:
            print(f"Transaction validation failed: {error}")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
