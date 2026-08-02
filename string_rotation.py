str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Strings are Rotations")
else:
    print("Strings are Not Rotations")