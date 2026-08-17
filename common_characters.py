str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

common = ""

for ch in str1:
    if ch in str2 and ch not in common:
        common += ch

print("Common Characters:", common)