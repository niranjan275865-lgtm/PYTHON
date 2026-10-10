text = input("Enter a string: ")

result = ""

for char in text:
    if char.lower() not in "aeiou":
        result += char

print("String without vowels:", result)