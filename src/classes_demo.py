"""Build up classes step by step; each section runs independently."""


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print("1: Classes and Objects / Instances")
    print("2: Attributes")
    print("3: Understanding self")
    print("4: Constructors / __init__")
    print("5: Methods")
    print("6: Class vs Instance Attributes")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        # ==================================================
        # Classes and Objects / Instances
        # ==================================================
        print("--> Classes and Objects / Instances")

        # A class describes a kind of object. pass allows an empty class body.
        class Customer:
            pass

        # Each call creates a separate instance of the same class.
        customer_1 = Customer()
        customer_2 = Customer()
        print(f"customer_1: {customer_1}")
        print(f"customer_2: {customer_2}")
        print(f"customer_1 type: {type(customer_1)}")
        print(f"customer_2 type: {type(customer_2)}")
        print(f"same object: {customer_1 is customer_2}")

    elif selection == "2":
        # ==================================================
        # Attributes
        # ==================================================
        print("--> Attributes")

        class Customer:
            pass

        customer_1 = Customer()
        customer_2 = Customer()

        # Attributes can be added after creation and belong to that instance.
        customer_1.name = "Bob"
        customer_1.age = 20
        customer_2.name = "Alice"
        customer_2.age = 30
        print(f"customer_1: {customer_1.name}, {customer_1.age}")
        print(f"customer_2: {customer_2.name}, {customer_2.age}")

    elif selection == "3":
        # ==================================================
        # Understanding self
        # ==================================================
        print("--> Understanding self")

        class Customer:
            # self refers to the instance on which the method is called.
            def set_name(self, name):
                self.name = name

        customer_1 = Customer()
        customer_2 = Customer()
        # Python supplies self; we supply only the name argument.
        customer_1.set_name("Bob")
        customer_2.set_name("Alice")
        print(f"customer_1 name: {customer_1.name}")
        print(f"customer_2 name: {customer_2.name}")

    elif selection == "4":
        # ==================================================
        # Constructors / __init__
        # ==================================================
        print("--> Constructors / __init__")

        class Customer:
            # __init__ initializes a newly created instance automatically.
            # This avoids having to remember to assign attributes afterward.
            def __init__(self, name, age, city):
                self.name = name
                self.age = age
                self.city = city

        customer_1 = Customer("Bob", 20, "Chicago")
        customer_2 = Customer("Alice", 30, "Miami")
        print(f"customer_1: {customer_1.name}, {customer_1.age}, {customer_1.city}")
        print(f"customer_2: {customer_2.name}, {customer_2.age}, {customer_2.city}")

    elif selection == "5":
        # ==================================================
        # Methods
        # ==================================================
        print("--> Methods")

        class Customer:

            def __init__(self, name, age):
                self.name = name
                self.age = age

            # Methods are functions defined in a class and can use its data.
            def display_info(self):
                print(f"name: {self.name}")
                print(f"age: {self.age}")

        customer = Customer("Bob", 20)
        customer.display_info()

    elif selection == "6":
        # ==================================================
        # Class vs Instance Attributes
        # ==================================================
        print("--> Class vs Instance Attributes")

        class Customer:
            # A class attribute is shared unless an instance overrides it.
            customer_type = "Retail"

            def __init__(self, name):
                # Each instance stores its own name.
                self.name = name

        customer_1 = Customer("Bob")
        customer_2 = Customer("Alice")
        print(f"class default: {Customer.customer_type}")
        print(f"{customer_1.name}: {customer_1.customer_type}")
        print(f"{customer_2.name}: {customer_2.customer_type}")

        Customer.customer_type = "Member"
        print(f"after class change: {customer_1.customer_type}, {customer_2.customer_type}")

        # Assignment through an instance creates its own overriding attribute.
        customer_1.customer_type = "Wholesale"
        print(f"{customer_1.name}: {customer_1.customer_type}")
        print(f"{customer_2.name}: {customer_2.customer_type}")
        print(f"class default remains: {Customer.customer_type}")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
