total = int(input("Enter the total bill amount: "))
paid = int(input("Enter the paid amount: "))
left = total - paid
if left != 0:
    print("Amount left to be paid is Rs ",left)
else:
    print("Complete amount is paid!")