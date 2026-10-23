text = input("Enter a string: ")

if len(text) == len(set(text)):
    print("All characters are unique")
else:
    print("Duplicate characters found")