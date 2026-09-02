,sentence = input("Enter a Sentence: ")

words = sentence.split()
largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest Word:", largest)