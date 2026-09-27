import Classes.transaction as ts
from summary import display_summary, category_summary

trans = []

trans.append(ts.Transaction(1001, "Bob Smith", "Grocery", 75.50, "Approved", False))
trans.append(ts.Transaction(1002, "Alice Johnson", "Dining", 42.25, "Approved", False))
trans.append(ts.Transaction(1003, "Charlie Brown", "Travel", 1250.00, "Approved", True))
trans.append(ts.Transaction(1004, "David Miller", "Entertainment", 89.99, "Declined", False))
trans.append(ts.Transaction(1005, "Emma Davis", "Other", 15.00, "Pending", False))
trans.append(ts.Transaction(1006, "Frank Wilson", "Grocery", 132.40, "Approved", False))
trans.append(ts.Transaction(1007, "Grace Lee", "Travel", 640.00, "Approved", True))
trans.append(ts.Transaction(1008, "Henry Clark", "Dining", 58.75, "Approved", False))
trans.append(ts.Transaction(1009, "Isabella Moore", "Entertainment", 120.00, "Approved", False))
trans.append(ts.Transaction(1010, "Jack Taylor", "Grocery", 210.35, "Declined", False))
trans.append(ts.Transaction(1011, "Karen Anderson", "Travel", 2200.00, "Approved", True))
trans.append(ts.Transaction(1012, "", "Dining", 55.00, "Approved", False))
trans.append(ts.Transaction(1013, "Laura Thomas", "InvalidCategory", 80.00, "Approved", False))
trans.append(ts.Transaction(1014, "Michael Jackson", "Other", -25.00, "Approved", False))
trans.append(ts.Transaction(1015, "Nancy White", "Grocery", 95.00, "Unknown", False))

print("Please select an option:")
print("1.Display all transactions")
print("2.Display valid transactions")
print("3.Display invalid transactions")
print("4.Display transaction summary")
print("5.Display category summary")
print("6.Search for a transaction by ID")
print("7.Exit")
print("")
selection = input("Enter option number: ")
try:
    if int(selection)>0 and int(selection)<8:
        if selection == "1":
            for tran in trans:
                tran.displaytransaction()
        if selection == "2":
            for tran in trans:
                if len(tran.is_valid()) == 0:
                    tran.displaytransaction()
        if selection == "3":
            for tran in trans:
                is_valid = tran.is_valid()
                if len(is_valid) > 0:
                    print(f"For transaction_ID:{tran.transaction_id} invalid failures:")
                    print(is_valid)
        if selection == "4":
            display_summary(trans)
        if selection == "5":
            category_summary(trans)
        if selection == "6":
            print("Search based on transaction id")
            searchid = input("Enter transaction id:")
            try:
                if int(searchid)>0:
                    for tran in trans:
                        if tran.transactionsearch(searchid):
                            tran.displaytransaction()
                else:
                    print("value needs to be positive")
            except Exception as error:
                print("please enter a numeric value for transaction id")
    else:
        print("please enter a value between 1-7")     
except Exception as error:
    print("There was an error")
        

