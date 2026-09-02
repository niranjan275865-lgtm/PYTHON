base = int(input("Enter Base: "))
exponent = int(input("Enter Exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("Result =", result)