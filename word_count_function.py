def word_count(sentence):

    words = sentence.split()

    return len(words)


text = input("Enter a sentence: ")

result = word_count(text)

print("Number of Words:", result)