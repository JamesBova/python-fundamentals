"""Conditions, loops, break, and continue."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: If / Elif / Else")
    print("2: For Loops")
    print("3: While Loops")
    print("4: Break")
    print("5: Continue")

    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # If / Elif / Else
        # ==================================================
        print("--> If / Elif / Else")

        # Multiple conditions with elif
        score = 85

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"score: {score}")
        print(f"grade: {grade}")

        # AND
        age = 20
        has_id = True

        if age >= 18 and has_id:
            print("Entry allowed.")
        else:
            print("Entry denied.")

        # OR
        is_admin = False
        is_owner = True

        if is_admin or is_owner:
            print("Access granted.")
        else:
            print("Access denied.")

        # Test a Boolean directly
        is_active = True

        if is_active:
            print("Account is active.")
        else:
            print("Account is inactive.")

        # Nested if statements
        age = 20
        has_id = True

        if age >= 18:
            print("Age requirement passed.")

            if has_id:
                print("ID requirement passed.")
                print("Entry allowed.")
            else:
                print("Entry denied: ID required.")
        else:
            print("Entry denied: must be 18 or older.")

    elif selection == "2":
        # ==================================================
        # For Loops
        # ==================================================
        print("--> For Loops")

        # Loop through a list
        names = ["Bob", "Alice", "Charlie"]

        for name in names:
            print(f"name: {name}")

        # Loop through a range of numbers
        for number in range(5):
            print(f"range(5): {number}")

        # Specify start and stop values
        for number in range(1, 6):
            print(f"range(1, 6): {number}")

        # Specify start, stop, and step
        for number in range(0, 10, 2):
            print(f"even number: {number}")

        # Perform calculations inside a loop
        prices = [10, 20, 30]

        for price in prices:
            price_with_tax = price * 1.10
            print(f"price: {price}, with tax: {price_with_tax}")

        # Combine a for loop with an if statement
        numbers = [10, 15, 20, 25, 30]

        for number in numbers:
            if number >= 20:
                print(f"{number} is 20 or greater")

        # Loop through characters in a string
        word = "Python"

        for letter in word:
            print(f"letter: {letter}")

        # Loop through dictionary key/value pairs
        person = {
            "name": "Bob",
            "age": 20,
            "city": "Chicago"
        }

        for key, value in person.items():
            print(f"{key}: {value}")

        # Use enumerate() to get both an index and a value
        names = ["Bob", "Alice", "Charlie"]

        for index, name in enumerate(names):
            print(f"index: {index}, name: {name}")

        # Start enumerate() at 1 instead of 0
        for index, name in enumerate(names, start=1):
            print(f"{index}. {name}")

        # Nested loops
        departments = ["Sales", "IT"]
        employees = ["Bob", "Alice"]

        for department in departments:
            for employee in employees:
                print(f"employee: {employee}, department: {department}")

    elif selection == "3":
        # ==================================================
        # While Loops
        # ==================================================
        print("--> While Loops")

        # Basic while loop
        count = 1

        while count <= 5:
            print(f"count: {count}")
            count += 1

        # Count downward
        count = 5

        while count > 0:
            print(f"countdown: {count}")
            count -= 1

        # Use a Boolean to control the loop
        is_running = True
        count = 1

        while is_running:
            print(f"count: {count}")

            count += 1

            if count > 3:
                is_running = False

        # Continue asking until the correct value is entered
        password = ""

        while password != "python":
            password = input("Enter the practice password (python): ")

        print("Correct password.")

        # A while loop continues until its condition becomes False.
        # Be careful to update the condition inside the loop.
        # Otherwise, an infinite loop can occur.

    elif selection == "4":
        # ==================================================
        # Break
        # ==================================================
        print("--> Break")

        # Stop searching once the desired file is found
        files = [
            "accounts.csv",
            "customers.csv",
            "transactions.csv",
            "merchants.csv"
        ]

        for filename in files:
            print(f"checking: {filename}")

            if filename == "transactions.csv":
                print(f"found file: {filename}")
                break

        # Break out of an otherwise infinite while loop
        count = 1

        while True:
            print(f"count: {count}")

            if count == 5:
                print("Reached 5 - stopping loop")
                break

            count += 1

        # Break only exits the loop it directly belongs to
        for department in ["IT", "Sales"]:
            for employee in ["Bob", "Alice", "Charlie"]:

                if employee == "Alice":
                    break

                print(f"{department}: {employee}")

    elif selection == "5":
        # ==================================================
        # Continue
        # ==================================================
        print("--> Continue")

        # Skip one value and continue the loop
        numbers = [10, 20, 30, 40, 50]

        for number in numbers:
            if number == 30:
                print("Skipping 30")
                continue

            print(f"number: {number}")

        # Skip files that are not CSV files
        files = [
            "accounts.csv",
            "notes.txt",
            "transactions.csv",
            "readme.md"
        ]

        for filename in files:
            if not filename.endswith(".csv"):
                continue

            print(f"processing CSV file: {filename}")

        # Continue also works with while loops
        count = 0

        while count < 5:
            count += 1

            if count == 3:
                continue

            print(f"count: {count}")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
