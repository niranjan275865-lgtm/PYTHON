text = input("Enter a String: ")

count = 0

for ch in text:
    if not ch.isalnum() and ch != " ":
        count += 1

print("Special Characters:", count)