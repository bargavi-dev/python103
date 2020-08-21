total_bill = float(input('Total bill amount?'))
level_of_service = input('Level of service?')
tip_amount = total_bill * (.10 or .20 or .15)
total_amount = total_bill + tip_amount

if level_of_service == "good":
    tip_amount == (.10 * total_bill)
    print("Tip amount:" + str((.20 * total_bill)))
elif level_of_service == "fair":
    (tip_amount == .15 * total_bill)
    print("Tip amount:" + str((.15 * total_bill)))
else:
    tip_amount == (.10 * total_bill)
    print("Tip amount:" + str((.10 * total_bill)))
print(total_amount)