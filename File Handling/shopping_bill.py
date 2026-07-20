amount = float(input("Enter Shopping Amount: "))

if amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

final_bill = amount - discount

print("Discount =", discount)
print("Final Bill =", final_bill)