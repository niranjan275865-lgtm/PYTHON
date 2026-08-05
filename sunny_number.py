import math

num = int(input("Enter a Number: "))

root = math.sqrt(num + 1)

if root == int(root):
    print("Sunny Number")
else:
    print("Not a Sunny Number")