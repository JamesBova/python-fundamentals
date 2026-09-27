"""Function definitions, arguments, return values, scope, and type hints."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Function Definitions")
    print("2: Parameters and Arguments")
    print("3: Return Values")
    print("4: Scope")
    print("5: Default Arguments")
    print("6: Basic Type Hints")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Function Definitions
        # ==================================================
        print("--> Function Definitions")

        # Define a basic function
        def say_hello():
            print("Hello!")

        say_hello()

        # A function can be called multiple times
        def print_message():
            print("Processing data...")

        print_message()
        print_message()

        # Functions can contain multiple statements
        def print_start_message():
            print("--------------------")
            print("Processing started")
            print("--------------------")

        print_start_message()

        # Functions can contain control flow
        def check_age():
            age = 20
            if age >= 18:
                print("Person is an adult.")
            else:
                print("Person is a minor.")

        check_age()

        # Functions can contain loops
        def print_names():
            names = ["Bob", "Alice", "Charlie"]
            for name in names:
                print(f"name: {name}")

        print_names()

    elif selection == "2":
        # ==================================================
        # Parameters and Arguments
        # ==================================================
        print("--> Parameters and Arguments")

        # Function with one parameter
        def say_hello(name):
            print(f"Hello, {name}!")

        say_hello("Bob")
        say_hello("Alice")

        # Function with multiple parameters
        def display_person(name, age):
            print(f"name: {name}")
            print(f"age: {age}")

        display_person("Bob", 20)
        display_person("Alice", 30)
        # Positional arguments
        # Values are matched to parameters based on their position.
        display_person("Charlie", 25)
        # Keyword arguments
        # Values are matched to parameters by name.
        display_person(age=40, name="David")

        # Use parameters in calculations
        def calculate_total(price, quantity):
            total = price * quantity
            print(f"price: {price}")
            print(f"quantity: {quantity}")
            print(f"total: {total}")

        calculate_total(10, 3)
        calculate_total(25, 4)

        # Use a parameter with an if statement
        def check_age(age):
            if age >= 18:
                print(f"{age}: adult")
            else:
                print(f"{age}: minor")

        check_age(20)
        check_age(15)

        # Pass a list into a function
        def print_names(names):
            for name in names:
                print(f"name: {name}")

        people = ["Bob", "Alice", "Charlie"]
        print_names(people)

    elif selection == "3":
        # ==================================================
        # Return Values
        # ==================================================
        print("--> Return Values")

        # Return a calculated value
        def add_numbers(a, b):
            total = a + b
            return total

        result = add_numbers(10, 5)
        print(f"result: {result}")

        # Use a returned value in additional calculations
        def calculate_total(price, quantity):
            return price * quantity

        total = calculate_total(10, 3)
        tax = total * 0.10
        grand_total = total + tax
        print(f"total: {total}")
        print(f"tax: {tax}")
        print(f"grand total: {grand_total}")

        # Return a string
        def get_age_group(age):
            if age >= 18:
                return "adult"
            else:
                return "minor"

        age_group = get_age_group(20)
        print(f"age group: {age_group}")

        # Return a Boolean value
        def is_adult(age):
            return age >= 18

        result = is_adult(20)
        print(f"is adult: {result}")

        # Return immediately exits the function
        def check_number(number):
            if number < 0:
                return "negative"
            print("Number was not negative.")
            return "zero or positive"

        result = check_number(10)
        print(f"result: {result}")

    elif selection == "4":
        # ==================================================
        # Scope
        # ==================================================
        print("--> Scope")

        # Local variable
        # A variable created inside a function normally exists
        # only inside that function.
        def show_message():
            message = "Hello from the function"
            print(f"inside function: {message}")

        show_message()

        # Parameters are also local variables
        def say_hello(name):
            print(f"name inside function: {name}")

        say_hello("Bob")

        company = "ABC Company"

        def show_company():
            print(f"company inside function: {company}")

        show_company()
        print(f"company outside function: {company}")

        # Local and global variables can have the same name.
        name = "Bob"

        def show_different_name():
            name = "Alice"
            print(f"name inside function: {name}")

        show_different_name()
        print(f"name outside function: {name}")

        # Use global to modify a global variable.
        count = 10

        def change_count():
            global count
            count = 20

        change_count()
        print(f"count after function: {count}")

        # It is usually cleaner to pass a value into a function
        # and return the new value instead of modifying a global variable.
        def increase_count(count):
            return count + 1

        count = 10
        count = increase_count(count)

        print(f"count returned from function: {count}")

    elif selection == "5":
        # ==================================================
        # Default Arguments
        # ==================================================
        print("--> Default Arguments")

        def say_hello(name="Guest"):
            print(f"Hello, {name}!")

        say_hello()
        say_hello("Bob")

        def display_person(name, city="Chicago"):
            print(f"name: {name}")
            print(f"city: {city}")

        display_person("Bob")
        display_person("Alice", "Miami")
        # Required parameters come before parameters with defaults.

        def create_user(name, age=18, active=True):
            print(f"name: {name}")
            print(f"age: {age}")
            print(f"active: {active}")

        create_user("Bob")
        create_user("Alice", 30, False)  # Override the defaults.
        create_user("Charlie", active=False)  # Override just one default by name.

    elif selection == "6":
        # ==================================================
        # Basic Type Hints
        # ==================================================
        print("--> Basic Type Hints")

        # Type hints for parameters
        def say_hello(name: str) -> None:
            print(f"Hello, {name}!")

        say_hello("Bob")

        # Parameter and return type hints
        def add_numbers(a: int, b: int) -> int:
            return a + b

        result = add_numbers(10, 5)
        print(f"result: {result}")

        # String return type
        def get_full_name(first_name: str, last_name: str) -> str:
            return f"{first_name} {last_name}"

        full_name = get_full_name("Bob", "Smith")
        print(f"full name: {full_name}")

        # Boolean return type
        def is_adult(age: int) -> bool:
            return age >= 18

        result = is_adult(20)
        print(f"is adult: {result}")

        # Float parameter and return type
        def calculate_tax(amount: float, tax_rate: float) -> float:
            return amount * tax_rate

        tax = calculate_tax(100.00, 0.10)
        print(f"tax: {tax}")

        # List type hint
        def print_names(names: list[str]) -> None:
            for name in names:
                print(f"name: {name}")

        people = ["Bob", "Alice", "Charlie"]
        print_names(people)

        # List input with an integer return value
        def total_numbers(numbers: list[int]) -> int:
            return sum(numbers)

        numbers = [10, 20, 30]
        total = total_numbers(numbers)
        print(f"total: {total}")

        # Type hints describe the expected types.
        # Python does not enforce them automatically at runtime.

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
