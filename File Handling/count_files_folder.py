import os

files = os.listdir(".")

count = 0

for file in files:
    if os.path.isfile(file):
        count += 1

print("Number of Files:", count)