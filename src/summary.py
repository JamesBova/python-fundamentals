def display_summary(trans: list):
    print(f"Count of records:{sum(1 for rec in trans)}")
    print(f"Valid Count of records:{sum(1 for rec in trans if len(rec.is_valid())==0)}")
    print(f"Invalid Count of records:{sum(1 for rec in trans if len(rec.is_valid())>0)}")
    print("Status Record Count:")
    print(f"     Approved:{sum(1 for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0)}")
    print(f"     Declined:{sum(1 for rec in trans if rec.status.upper() == 'DECLINED' and len(rec.is_valid()) == 0)}")
    print(f"     Pending:{sum(1 for rec in trans if rec.status.upper() == 'PENDING' and len(rec.is_valid()) == 0)}")
    print(f"Total approved amount:{sum(rec.amount for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0):.2f}")
    if sum(1 for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0)>0:
        print(f"Average approved amount:{sum(rec.amount for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0)/sum(1 for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0):.2f}")
        print(f"Largest approved amount:{max(rec.amount for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0):.2f}")
        print(f"Smallest approved amount:{min(rec.amount for rec in trans if rec.status.upper() == 'APPROVED' and len(rec.is_valid()) == 0):.2f}")
            
    else:
        print("Average approved amount: there are no approved amounts")
        print("Largest approved amount: there are no approved amounts")
        print("Smallest approved amount: there are no approved amounts")
    print(f"Total international transaction count:{sum(1 for rec in trans if rec.is_international and len(rec.is_valid()) == 0)}")
def category_summary(trans: list):
    category=[]
    for tran in trans:
        if len(tran.is_valid()) == 0 and tran.status.upper() == "APPROVED":
            category.append(tran.category)
    categoryset = sorted(set(category))
    #print(categoryset)
    for cat in categoryset:
        print(f"Category: {cat}")

        approved_count = sum(
            1 for rec in trans
            if rec.status.upper() == "APPROVED" and rec.category == cat and len(rec.is_valid()) == 0
        )

        approved_total = sum(
            rec.amount for rec in trans
            if rec.status.upper() == "APPROVED" and rec.category == cat and len(rec.is_valid()) == 0
        )

        print(f"     Approved transaction count:{approved_count}")
        print(f"     Total approved amount:{approved_total:.2f}")

        if approved_count > 0:
            print(f"     Average approved amount: {approved_total / approved_count:.2f}")
        else:
            print("     Average approved amount: 0.00")