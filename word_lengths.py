sentence = input("Enter a Sentence: ")

words = sentence.split()

for word in words:
    print(word, "=", len(word))