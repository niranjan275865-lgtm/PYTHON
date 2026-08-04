num = int(input("Enter a Number: "))

square = num * num

if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")