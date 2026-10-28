from collections import Counter

text = input("Enter a string: ")

if text:
    counts = Counter(text)
    character, frequency = counts.most_common(1)[0]

    print("Most frequent character:", character)
    print("Frequency:", frequency)
else:
    print("Please enter a non-empty string")