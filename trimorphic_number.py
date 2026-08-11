num = int(input("Enter a Number: "))

cube = num ** 3

if str(cube).endswith(str(num)):
    print("Trimorphic Number")
else:
    print("Not a Trimorphic Number")