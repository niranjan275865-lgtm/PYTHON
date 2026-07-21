num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
op = input("Enter Operator (+, -, *, /): ")

if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    print("Result =", num1 / num2)
else:
    print("Invalid Operator")