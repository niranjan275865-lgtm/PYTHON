sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("Please enter a sentence")