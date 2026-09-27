"""Transaction exercise combining the concepts in the standalone lessons."""

from Classes.transaction import Transaction
from summary import category_summary, display_summary


# Importing this module does not create sample records or ask for input.
if __name__ == "__main__":
    # ==================================================
    # Sample Transactions
    # ==================================================
    # Keep invalid records so the validation examples have failures to report.
    transactions = []

    transactions.append(Transaction(1001, "Bob Smith", "Grocery", 75.50, "Approved", False))
    transactions.append(Transaction(1002, "Alice Johnson", "Dining", 42.25, "Approved", False))
    transactions.append(Transaction(1003, "Charlie Brown", "Travel", 1250.00, "Approved", True))
    transactions.append(Transaction(1004, "David Miller", "Entertainment", 89.99, "Declined", False))
    transactions.append(Transaction(1005, "Emma Davis", "Other", 15.00, "Pending", False))
    transactions.append(Transaction(1006, "Frank Wilson", "Grocery", 132.40, "Approved", False))
    transactions.append(Transaction(1007, "Grace Lee", "Travel", 640.00, "Approved", True))
    transactions.append(Transaction(1008, "Henry Clark", "Dining", 58.75, "Approved", False))
    transactions.append(Transaction(1009, "Isabella Moore", "Entertainment", 120.00, "Approved", False))
    transactions.append(Transaction(1010, "Jack Taylor", "Grocery", 210.35, "Declined", False))
    transactions.append(Transaction(1011, "Karen Anderson", "Travel", 2200.00, "Approved", True))
    transactions.append(Transaction(1012, "", "Dining", 55.00, "Approved", False))
    transactions.append(Transaction(1013, "Laura Thomas", "InvalidCategory", 80.00, "Approved", False))
    transactions.append(Transaction(1014, "Michael Jackson", "Other", -25.00, "Approved", False))
    transactions.append(Transaction(1015, "Nancy White", "Grocery", 95.00, "Unknown", False))

    # ==================================================
    # Select an Example
    # ==================================================
    print("1: Display all transactions")
    print("2: Display valid transactions")
    print("3: Display invalid transactions")
    print("4: Display transaction summary")
    print("5: Display category summary")
    print("6: Search for a transaction by ID")
    print("0: Exit")

    selection = input("Choose a section number: ").strip()

    if selection == "1":
        for transaction in transactions:
            transaction.display_transaction()

    elif selection == "2":
        for transaction in transactions:
            if transaction.is_valid():
                transaction.display_transaction()

    elif selection == "3":
        for transaction in transactions:
            errors = transaction.validation_errors()
            if errors:
                print(f"Transaction {transaction.transaction_id} validation failures:")
                print(errors)

    elif selection == "4":
        display_summary(transactions)

    elif selection == "5":
        category_summary(transactions)

    elif selection == "6":
        # Catch conversion errors only; other programming errors should stay visible.
        try:
            search_id = int(input("Enter transaction ID: "))
        except ValueError:
            print("Please enter a whole number for the transaction ID.")
        else:
            if search_id <= 0:
                print("Transaction ID must be positive.")
            else:
                found = False
                for transaction in transactions:
                    if transaction.matches_id(search_id):
                        transaction.display_transaction()
                        found = True
                        break
                if not found:
                    print(f"No transaction found with ID {search_id}.")

    elif selection == "0":
        print("Goodbye!")
    else:
        print("Invalid selection. Choose one of the listed numbers.")
