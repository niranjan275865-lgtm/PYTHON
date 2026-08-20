text = input("Enter a String: ")

count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print("Number of Digits:", count)