"""Lists, tuples, sets, and dictionaries."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Lists")
    print("2: Tuples")
    print("3: Sets")
    print("4: Dictionaries")

    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Lists
        # ==================================================
        print("--> Lists")

        # Lists are ordered and mutable (their contents can change).
        names = ["Bob", "Alice", "Charlie"]
        print(f"names: {names}")

        # Access values by index
        print(f"first name: {names[0]}")
        print(f"second name: {names[1]}")
        print(f"last name: {names[-1]}")

        # Change an existing value
        names[0] = "Robert"
        print(f"after changing first item: {names}")

        # Add values
        names.append("David")
        print(f"after append: {names}")

        names.insert(1, "Susan")
        print(f"after insert: {names}")

        # Remove values
        names.remove("Alice")
        print(f"after remove: {names}")

        removed_name = names.pop(0)
        print(f"removed name: {removed_name}")
        print(f"after pop: {names}")

        # List length
        print(f"number of names: {len(names)}")

        # Check whether values exist
        print(f"'Charlie' in names: {'Charlie' in names}")
        print(f"'Bob' in names: {'Bob' in names}")

        # Lists can contain different data types
        record = ["Bob", 20, True, 10.50]
        print(f"record: {record}")

        # Nested lists
        customers = [
            ["Bob", 20],
            ["Alice", 30],
            ["Charlie", 25]
        ]

        print(f"first customer: {customers[0]}")
        print(f"first customer's name: {customers[0][0]}")

        # List slicing
        numbers = [10, 20, 30, 40, 50]

        print(f"numbers: {numbers}")
        print(f"first three: {numbers[0:3]}")
        print(f"from index 2 onward: {numbers[2:]}")
        print(f"first three shorthand: {numbers[:3]}")

        # The ending slice index is not included.
        # numbers[0:3] returns indexes 0, 1, and 2.

        # Sorting
        numbers = [50, 10, 40, 20, 30]

        numbers.sort()
        print(f"sorted numbers: {numbers}")

        numbers.sort(reverse=True)
        print(f"reverse sorted numbers: {numbers}")

    elif selection == "2":
        # ==================================================
        # Tuples
        # ==================================================
        print("--> Tuples")

        # Tuples are ordered; their items cannot be reassigned.
        colors = ("red", "green", "blue", "purple")

        print(f"colors: {colors}")
        print(f"tuple type: {type(colors)}")

        # Access values by index
        print(f"first color: {colors[0]}")
        print(f"second color: {colors[1]}")
        print(f"last color: {colors[-1]}")

        # Tuple slicing
        numbers = (10, 20, 30, 40, 50)

        print(f"numbers: {numbers}")
        print(f"first three numbers: {numbers[:3]}")
        print(f"numbers from index 2 onward: {numbers[2:]}")

        # Tuple length
        print(f"number of colors: {len(colors)}")

        # Check whether values exist
        print(f"'green' in colors: {'green' in colors}")
        print(f"'yellow' in colors: {'yellow' in colors}")

        # Count occurrences of a value
        values = (10, 20, 10, 30, 10)

        print(f"values: {values}")
        print(f"number of times 10 appears: {values.count(10)}")

        # Find the index of a value
        print(f"index of 30: {values.index(30)}")

        # Tuple unpacking
        person = ("Bob", 20, "Chicago")

        name, age, city = person

        print(f"name: {name}")
        print(f"age: {age}")
        print(f"city: {city}")

        # Tuples can contain different data types
        record = ("Bob", 20, True, 10.50)
        print(f"record: {record}")

        # Nested tuples
        locations = (
            ("Chicago", "Illinois"),
            ("Miami", "Florida"),
            ("Pittsburgh", "Pennsylvania")
        )

        print(f"locations: {locations}")
        print(f"first location: {locations[0]}")
        print(f"first city: {locations[0][0]}")
        print(f"first state: {locations[0][1]}")

        # The comma makes this a tuple, rather than a parenthesized number.
        single_value = (10,)

        print(f"single value: {single_value}")
        print(f"single value type: {type(single_value)}")

        # Tuples are immutable.
        # This would cause an error:
        # colors[0] = "yellow"

    elif selection == "3":
        # ==================================================
        # Sets
        # ==================================================
        print("--> Sets")

        # Sets hold unique values; their display order can vary.
        colors = {"red", "green", "blue"}

        print(f"colors: {colors}")
        print(f"set type: {type(colors)}")

        # Duplicate values are automatically removed
        numbers = {10, 20, 10, 30, 20}
        print(f"numbers with duplicates removed: {numbers}")

        # Add a value
        colors.add("yellow")
        print(f"after add: {colors}")

        # Remove a value
        colors.remove("green")
        print(f"after remove: {colors}")

        # Check whether values exist
        print(f"'red' in colors: {'red' in colors}")
        print(f"'purple' in colors: {'purple' in colors}")

        # Number of unique values
        print(f"number of colors: {len(colors)}")

        # Sets are unordered and do not support indexing.
        # This would cause an error:
        # print(colors[0])

    elif selection == "4":
        # ==================================================
        # Dictionaries
        # ==================================================
        print("--> Dictionaries")

        # Dictionaries associate unique keys with values.
        person = {
            "name": "Bob",
            "age": 20,
            "city": "Chicago"
        }

        print(f"person: {person}")

        # Access values by key
        print(f"name: {person['name']}")
        print(f"age: {person['age']}")
        print(f"city: {person['city']}")

        # Change an existing value
        person["age"] = 21
        print(f"updated age: {person['age']}")

        # Add a new key/value pair
        person["is_active"] = True
        print(f"after adding is_active: {person}")

        # Remove a key/value pair
        person.pop("city")
        print(f"after removing city: {person}")

        # Safely retrieve values with get()
        # get() returns None instead of causing an error if the key does not exist.
        print(f"name using get(): {person.get('name')}")
        print(f"email using get(): {person.get('email')}")

        # Provide a default value if the key does not exist
        email = person.get("email", "No email provided")
        print(f"email with default: {email}")

        # Check whether keys exist
        print(f"'name' in person: {'name' in person}")
        print(f"'email' in person: {'email' in person}")

        # Get dictionary keys, values, and key/value pairs
        print(f"keys: {person.keys()}")
        print(f"values: {person.values()}")
        print(f"items: {person.items()}")

        # Loop through key/value pairs.
        # Uses a for loop, which is covered in control_flow.py.
        for key, value in person.items():
            print(f"{key}: {value}")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
