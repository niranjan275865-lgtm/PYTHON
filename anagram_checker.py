str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")