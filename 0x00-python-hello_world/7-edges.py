#!/usr/bin/python3
word = "Holberton"
print(f"First 3 letters: {word[:3]}")
print(f"Last 2 letters: {word[-2:]}")
rm_first = word[1:]
middle_word = rm_first[:-1]
print(f"Middle word: {middle_word}")
