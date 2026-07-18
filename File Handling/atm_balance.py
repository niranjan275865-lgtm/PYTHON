balance = 5000

amount = int(input("Enter Withdrawal Amount: "))

if amount <= balance:
    balance = balance - amount
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")