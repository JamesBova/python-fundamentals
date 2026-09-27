class Transaction:
    def __init__(self,transaction_id,customer_name,category,amount,status,is_international):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.category = category
        self.amount = amount
        self.status = status
        self.is_international = is_international
    def displaytransaction(self):
        print("----------------")
        print(f"transaction_id: {self.transaction_id}")
        print(f"customer_name: {self.customer_name}")
        print(f"category: {self.category}")
        print(f"amount: {self.amount}")
        print(f"status: {self.status}")
        print(f"is_international: {self.is_international}")
        print(f"Is valid transaction: {len(self.is_valid())==0}")
        if len(self.is_valid())==0:
            print(f"Is high value: {self.is_high_value()}")
            print(f"International fee: {self.international_fee()}")
            print(f"requires review: {self.requires_review()}")
        else:
            print(f"Invalid reason: {self.is_valid()}")

    def is_valid(self) -> str:
        rvalue = ""
        if type(self.transaction_id) != int:
            rvalue += "Transaction_ID is not an integer\n"
        elif self.transaction_id <= 0:
            rvalue += "Transaction_ID is <= 0\n"
        if self.customer_name.strip() == "":
            rvalue = rvalue + "Customer Name is blank\n"
        if self.category.upper() not in ["GROCERY","DINING","TRAVEL","ENTERTAINMENT","OTHER"]:
            rvalue = rvalue + "category is invalid\n"
        if self.amount<=0:
            rvalue = rvalue + "amount is less than or equal to 0\n"
        if self.status.upper() not in ['APPROVED','DECLINED','PENDING']:
            rvalue = rvalue + self.status + " is not 'Approved','Declined' or 'Pending'\n"
        if type(self.is_international) != bool:
            rvalue = rvalue + "is_international is not a boolean\n"
        return rvalue
    def transactionsearch(self, transactionid) -> bool:
        return int(self.transaction_id) == int(transactionid)
    def is_high_value(self)-> bool:
        return self.amount >= 1000
    def international_fee(self) -> float:
        if self.status.upper() == "APPROVED" and self.is_international:
            return self.amount * .03
        else:
            return 0.0
    def requires_review(self)-> bool:
        return self.is_international and self.amount >= 500
        