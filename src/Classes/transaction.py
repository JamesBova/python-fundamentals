"""Transaction attributes, validation, and simple business-rule methods."""


class Transaction:
    def __init__(
        self, transaction_id, customer_name, category, amount, status, is_international
    ):
        # Store the supplied values, including invalid ones, for validation practice.
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.category = category
        self.amount = amount
        self.status = status
        self.is_international = is_international

    def display_transaction(self) -> None:
        errors = self.validation_errors()
        print("----------------")
        print(f"transaction_id: {self.transaction_id}")
        print(f"customer_name: {self.customer_name}")
        print(f"category: {self.category}")
        print(f"amount: {self.amount}")
        print(f"status: {self.status}")
        print(f"is_international: {self.is_international}")
        print(f"Is valid transaction: {errors == ''}")
        if not errors:
            print(f"Is high value: {self.is_high_value()}")
            print(f"International fee: {self.international_fee():.2f}")
            print(f"Requires review: {self.requires_review()}")
        else:
            print(f"Invalid reasons:\n{errors}")

    def validation_errors(self) -> str:
        """Return all validation messages, or an empty string for a valid record."""
        errors = ""
        # Exact type checks keep True/False from being accepted as numeric values.
        if type(self.transaction_id) is not int:
            errors += "Transaction ID must be an integer.\n"
        elif self.transaction_id <= 0:
            errors += "Transaction ID must be positive.\n"

        # Check types before calling string methods or comparing numbers.
        if not isinstance(self.customer_name, str):
            errors += "Customer name must be a string.\n"
        elif self.customer_name.strip() == "":
            errors += "Customer name is blank.\n"

        if not isinstance(self.category, str):
            errors += "Category must be a string.\n"
        elif self.category.upper() not in [
            "GROCERY", "DINING", "TRAVEL", "ENTERTAINMENT", "OTHER"
        ]:
            errors += "Category is invalid.\n"

        if type(self.amount) not in (int, float):
            errors += "Amount must be a number.\n"
        elif not 0 < self.amount < float("inf"):
            # This also rejects non-finite float values such as nan and infinity.
            errors += "Amount must be positive and finite.\n"

        if not isinstance(self.status, str):
            errors += "Status must be a string.\n"
        elif self.status.upper() not in ["APPROVED", "DECLINED", "PENDING"]:
            errors += "Status must be Approved, Declined, or Pending.\n"

        if type(self.is_international) is not bool:
            errors += "is_international must be a Boolean.\n"
        return errors

    def is_valid(self) -> bool:
        """A Boolean result makes validation usable directly in an if statement."""
        return self.validation_errors() == ""

    def matches_id(self, transaction_id: int) -> bool:
        # Convert user input before calling this method; compare IDs as integers.
        return type(self.transaction_id) is int and self.transaction_id == transaction_id

    # These calculation methods expect a valid transaction.
    # display_transaction() checks validation before using them.
    def is_high_value(self) -> bool:
        return self.amount >= 1000

    def international_fee(self) -> float:
        if self.status.upper() == "APPROVED" and self.is_international:
            return self.amount * 0.03
        else:
            return 0.0

    def requires_review(self) -> bool:
        return self.is_international and self.amount >= 500
