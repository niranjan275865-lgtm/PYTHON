text = input("Enter a String: ")

sum = 0

for ch in text:
    if ch.isdigit():
        sum += int(ch)

print("Sum of Digits:", sum)