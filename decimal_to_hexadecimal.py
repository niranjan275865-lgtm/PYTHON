num = int(input("Enter a decimal number: "))

if num >= 0:
    hexadecimal = hex(num)[2:].upper()
    print("Hexadecimal number:", hexadecimal)
else:
    print("Please enter a non-negative number")