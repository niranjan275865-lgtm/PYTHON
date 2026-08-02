import string

text = input("Enter a Sentence: ").lower()

if set(string.ascii_lowercase).issubset(set(text)):
    print("Pangram")
else:
    print("Not a Pangram")