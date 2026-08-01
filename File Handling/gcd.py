num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD =", num1)