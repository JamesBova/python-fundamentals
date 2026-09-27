"""Build, transform, and filter lists and dictionaries."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: List Comprehensions")
    print("2: Transforming Lists")
    print("3: Filtering Lists")
    print("4: Dictionary Comprehensions")
    print("5: Transforming Dictionaries")
    print("6: Filtering Dictionary Entries")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # List Comprehensions
        # ==================================================
        print("--> List Comprehensions")

        # Basic list comprehension
        numbers = [1, 2, 3, 4, 5]
        copied_numbers = [number for number in numbers]
        print(f"original numbers: {numbers}")
        print(f"copied numbers: {copied_numbers}")

    elif selection == "2":
        # ==================================================
        # Transforming Lists
        # ==================================================
        print("--> Transforming Lists")

        # Multiply each number by 2
        numbers = [1, 2, 3, 4, 5]
        doubled_numbers = [number * 2 for number in numbers]
        print(f"original numbers: {numbers}")
        print(f"doubled numbers: {doubled_numbers}")

        # Convert strings to uppercase
        names = ["Bob", "Alice", "Charlie"]
        uppercase_names = [name.upper() for name in names]
        print(f"original names: {names}")
        print(f"uppercase names: {uppercase_names}")

        # Perform calculations
        prices = [10, 20, 30]
        prices_with_tax = [price * 1.10 for price in prices]
        print(f"original prices: {prices}")
        print(f"prices with tax: {prices_with_tax}")

        # Transform each character in a string
        letters = [letter.upper() for letter in "hello"]
        print(f"uppercase letters: {letters}")

        # Create a list from a range
        numbers = [number for number in range(5)]
        print(f"numbers from range: {numbers}")

    elif selection == "3":
        # ==================================================
        # Filtering Lists
        # ==================================================
        print("--> Filtering Lists")

        # Keep only even numbers
        numbers = [1, 2, 3, 4, 5, 6]
        even_numbers = [
            number
            for number in numbers
            if number % 2 == 0
        ]
        print(f"original numbers: {numbers}")
        print(f"even numbers: {even_numbers}")

        # Keep only values greater than 20
        numbers = [10, 20, 30, 40, 50]
        large_numbers = [
            number
            for number in numbers
            if number > 20
        ]
        print(f"original numbers: {numbers}")
        print(f"numbers greater than 20: {large_numbers}")

        # Keep only CSV files
        files = [
            "accounts.csv",
            "notes.txt",
            "transactions.csv",
            "readme.md"
        ]
        csv_files = [
            filename
            for filename in files
            if filename.endswith(".csv")
        ]
        print(f"all files: {files}")
        print(f"CSV files: {csv_files}")

    elif selection == "4":
        # ==================================================
        # Dictionary Comprehensions
        # ==================================================
        print("--> Dictionary Comprehensions")

        # Create a dictionary from a list
        numbers = [1, 2, 3, 4, 5]
        squares = {
            number: number ** 2
            for number in numbers
        }
        print(f"numbers: {numbers}")
        print(f"squares: {squares}")

        # Create a dictionary from a list of names
        names = ["Bob", "Alice", "Charlie"]
        name_lengths = {
            name: len(name)
            for name in names
        }
        print(f"names: {names}")
        print(f"name lengths: {name_lengths}")

    elif selection == "5":
        # ==================================================
        # Transforming Dictionaries
        # ==================================================
        print("--> Transforming Dictionaries")

        prices = {
            "apple": 1.00,
            "banana": 0.50,
            "orange": 1.25
        }
        prices_with_tax = {
            item: price * 1.10
            for item, price in prices.items()
        }
        print(f"original prices: {prices}")
        print(f"prices with tax: {prices_with_tax}")

        # Transforming dictionary keys/values
        prices = {
            "apple": 1.00,
            "banana": 0.50,
            "orange": 1.25
        }
        transformed_prices = {
            item.upper(): round(price * 1.10, 2)
            for item, price in prices.items()
        }
        print(transformed_prices)

    elif selection == "6":
        # ==================================================
        # Filtering Dictionary Entries
        # ==================================================
        print("--> Filtering Dictionary Entries")

        # Keep entries based on their values
        prices = {
            "apple": 1.00,
            "banana": 0.50,
            "orange": 1.25,
            "grape": 2.00
        }
        expensive_items = {
            item: price
            for item, price in prices.items()
            if price >= 1.00
        }
        print(f"original prices: {prices}")
        print(f"items $1.00 or more: {expensive_items}")

        # Keep entries based on their keys
        people = {
            "Bob": 20,
            "Alice": 30,
            "Charlie": 25,
            "David": 40
        }
        names_starting_with_a = {
            name: age
            for name, age in people.items()
            if name.startswith("A")
        }
        print(f"all people: {people}")
        print(f"names starting with A: {names_starting_with_a}")

        # Filter and transform at the same time
        filtered_prices_with_tax = {
            item.upper(): round(price * 1.10, 2)
            for item, price in prices.items()
            if price >= 1.00
        }
        print(f"filtered and transformed: {filtered_prices_with_tax}")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
