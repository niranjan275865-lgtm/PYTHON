text = input("Enter a String: ")
ch = input("Enter Character: ")

count = 0

for c in text:
    if c == ch:
        count += 1

print("Frequency:", count)