text = input("Enter a String: ")

for ch in text:
    if text.count(ch) == 1:
        print("First Non-Repeated Character:", ch)
        break