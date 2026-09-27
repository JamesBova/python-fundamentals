"""Summary examples using filtering, loops, sets, and aggregate calculations."""

from Classes.transaction import Transaction


def display_summary(transactions: list[Transaction]) -> None:
    # Validate before accessing status or amounts in the calculations below.
    valid_transactions = [
        transaction for transaction in transactions if transaction.is_valid()
    ]
    approved_transactions = [
        transaction for transaction in valid_transactions
        if transaction.status.upper() == "APPROVED"
    ]
    approved_count = len(approved_transactions)
    approved_total = sum(transaction.amount for transaction in approved_transactions)

    print(f"Count of records: {len(transactions)}")
    print(f"Valid count of records: {len(valid_transactions)}")
    print(f"Invalid count of records: {len(transactions) - len(valid_transactions)}")
    print("Status record count (valid transactions only):")
    for status in ["Approved", "Declined", "Pending"]:
        count = sum(
            1 for transaction in valid_transactions
            if transaction.status.upper() == status.upper()
        )
        print(f"    {status}: {count}")

    print(f"Total approved amount: {approved_total:.2f}")
    # An empty list cannot be used with min/max or as a divisor.
    if approved_count > 0:
        largest_amount = max(transaction.amount for transaction in approved_transactions)
        smallest_amount = min(transaction.amount for transaction in approved_transactions)
        print(f"Average approved amount: {approved_total / approved_count:.2f}")
        print(f"Largest approved amount: {largest_amount:.2f}")
        print(f"Smallest approved amount: {smallest_amount:.2f}")
    else:
        print("Average approved amount: no approved transactions")
        print("Largest approved amount: no approved transactions")
        print("Smallest approved amount: no approved transactions")

    international_count = sum(
        1 for transaction in valid_transactions if transaction.is_international
    )
    print(f"International transaction count (valid only): {international_count}")


def category_summary(transactions: list[Transaction]) -> None:
    approved_transactions = [
        transaction for transaction in transactions
        if transaction.is_valid() and transaction.status.upper() == "APPROVED"
    ]
    if not approved_transactions:
        print("No valid approved transactions to summarize by category.")
        return

    # Preserve the list -> set -> sorted sequence as a collections example.
    categories = []
    for transaction in approved_transactions:
        categories.append(transaction.category.upper())
    unique_categories = sorted(set(categories))

    for category in unique_categories:
        # Normalize case consistently with the case-insensitive validation rule.
        category_transactions = [
            transaction for transaction in approved_transactions
            if transaction.category.upper() == category
        ]
        approved_count = len(category_transactions)
        approved_total = sum(transaction.amount for transaction in category_transactions)
        print(f"Category: {category.title()}")
        print(f"    Approved transaction count: {approved_count}")
        print(f"    Total approved amount: {approved_total:.2f}")
        # Each category came from an approved record, so its count is positive.
        print(f"    Average approved amount: {approved_total / approved_count:.2f}")
