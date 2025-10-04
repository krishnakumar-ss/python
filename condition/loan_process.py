high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
