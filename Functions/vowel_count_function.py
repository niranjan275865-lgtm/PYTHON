def count_vowels(s):
    count = 0

    for i in s:
        if i.lower() in "aeiou":
            count += 1

    return count

print(count_vowels("Education"))