"""Variables, data types, strings, numbers, and Booleans."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Variables")
    print("2: Data Types")
    print("3: Strings")
    print("4: Numbers")
    print("5: Booleans")

    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Variables
        # ==================================================
        print("--> Variables")

        # Variables give names to values and can be reassigned.
        name = "Bob"
        age = 20
        city = "Chicago"

        print(f"name: {name}")
        print(f"age: {age}")
        print(f"city: {city}")

        # Reassign an existing variable
        age = 21
        print(f"age after reassignment: {age}")

        # Use variables to calculate another value
        price = 10
        quantity = 3
        total = price * quantity

        print(f"price: {price}")
        print(f"quantity: {quantity}")
        print(f"total: {total}")

    elif selection == "2":
        # ==================================================
        # Data Types
        # ==================================================
        print("--> Data Types")

        # Common basic data types
        name = "Bob"        # str      -> string/text
        age = 20            # int      -> whole number
        price = 10.50       # float    -> decimal number
        is_active = True    # bool     -> True or False
        nothing = None      # NoneType -> represents no value

        # Check the type of each value
        print(f"name type: {type(name)}")
        print(f"age type: {type(age)}")
        print(f"price type: {type(price)}")
        print(f"is_active type: {type(is_active)}")
        print(f"nothing type: {type(nothing)}")

        # The same variable can hold different data types
        value = 10
        print(f"value = {value}, type: {type(value)}")

        value = "ten"
        print(f"value = {value}, type: {type(value)}")

    elif selection == "3":
        # ==================================================
        # Strings
        # ==================================================
        print("--> Strings")

        # Strings hold text; either single or double quotes work.
        first_name = "Bob"
        last_name = "Smith"

        print(f"first name: {first_name}")
        print(f"last name: {last_name}")

        # Combine strings
        full_name = first_name + " " + last_name
        print(f"full name: {full_name}")

        # Repeat a string
        word = "Hi "
        print(f"word repeated 3 times: {word * 3}")

        # Access individual characters by index
        name = "Rob"

        print(f"name[0]: {name[0]}")
        print(f"name[1]: {name[1]}")
        print(f"name[2]: {name[2]}")
        print(f"name[-1]: {name[-1]}")

        # Common string methods
        text = "  Hello World  "

        print(f"original text: '{text}'")
        print(f"lower(): {text.lower()}")
        print(f"upper(): {text.upper()}")
        print(f"strip(): {text.strip()}")
        print(f"replace(): {text.replace('World', 'Python')}")

        # Check the beginning and ending of a string
        filename = "transactions_20260923.csv"

        print(f"filename: {filename}")
        print(f"starts with 'transactions': {filename.startswith('transactions')}")
        print(f"ends with '.csv': {filename.endswith('.csv')}")

        # Split a string into multiple values
        parts = filename.split("_")
        print(f"split filename: {parts}")

        # Join multiple strings together
        words = ["Bob", "Smith", "is", "doing", "something"]

        combined_words = " ".join(words)
        print(f"joined words: {combined_words}")

        # Format strings using f-strings
        name = "Rob"
        age = 20

        print(f"f-string example: {name} is {age} years old.")

    elif selection == "4":
        # ==================================================
        # Numbers
        # ==================================================
        print("--> Numbers")

        # Integer and float
        age = 20
        price = 10.50

        print(f"age: {age}, type: {type(age)}")
        print(f"price: {price}, type: {type(price)}")

        # Basic arithmetic
        a = 10
        b = 3

        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} * {b} = {a * b}")
        print(f"{a} / {b} = {a / b}")

        # Division always returns a float
        print(f"10 / 2 = {10 / 2} (division always returns float)")

        # Additional mathematical operators
        print(f"10 // 3 = {10 // 3} (floor division)")
        print(f"10 % 3 = {10 % 3} (remainder)")
        print(f"2 ** 3 = {2 ** 3} (exponent)")

        # Convert an integer to a float
        number = 10
        decimal_number = float(number)

        print(f"original number: {number}")
        print(f"number converted to float: {decimal_number}")
        print(f"converted number type: {type(decimal_number)}")

        # int() truncates toward zero; it does not round
        price = 10.75
        whole_number = int(price)

        print(f"{price} converted to int: {whole_number}")

        # Round a number
        price = 10.756
        rounded_price = round(price, 2)

        print(f"{price} rounded to 2 decimal places: {rounded_price}")

        # Increment using normal assignment
        count = 10
        count = count + 1

        print(f"count after count = count + 1: {count}")

        # Assignment operators
        count = 10

        count += 1
        print(f"count after += 1: {count}")

        count -= 1
        print(f"count after -= 1: {count}")

        count *= 2
        print(f"count after *= 2: {count}")

        count /= 2
        print(f"count after /= 2: {count}")

    elif selection == "5":
        # ==================================================
        # Booleans
        # ==================================================
        print("--> Booleans")

        # Create Boolean values
        is_active = True
        is_deleted = False

        print(f"is_active: {is_active}")
        print(f"is_deleted: {is_deleted}")

        # Comparison operators produce Boolean results
        age = 20

        print(f"age == 20: {age == 20}")
        print(f"age != 20: {age != 20}")
        print(f"age > 18: {age > 18}")
        print(f"age < 18: {age < 18}")
        print(f"age >= 20: {age >= 20}")
        print(f"age <= 20: {age <= 20}")

        # AND
        # Both conditions must be True.
        has_id = True
        can_enter = age >= 18 and has_id

        print(f"age >= 18: {age >= 18}")
        print(f"has_id: {has_id}")
        print(f"can_enter using AND: {can_enter}")

        # OR
        # At least one condition must be True.
        is_admin = False
        is_owner = True
        has_access = is_admin or is_owner

        print(f"is_admin: {is_admin}")
        print(f"is_owner: {is_owner}")
        print(f"has_access using OR: {has_access}")

        # NOT
        # Reverses a Boolean value.
        is_active = True

        print(f"is_active: {is_active}")
        print(f"not is_active: {not is_active}")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
