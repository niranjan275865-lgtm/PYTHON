file = open("sample.txt", "r")

lines = file.readlines()

print("Last Line:", lines[-1].strip())

file.close()