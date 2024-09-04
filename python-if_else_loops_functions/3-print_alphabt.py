#!/usr/bin/python3
letters = ""
for letter in range(97, 122):
    if letter != 113 and letter != 101:
        letters += chr(letter)
print("{}".format(letters))
