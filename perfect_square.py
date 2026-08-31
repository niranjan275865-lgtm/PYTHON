import math

num = int(input("Enter a Number: "))

root = math.isqrt(num)

if root * root == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")