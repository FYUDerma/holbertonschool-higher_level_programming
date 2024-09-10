#!/usr/bin/python3
def multiple_returns(sentence):
    lng = len(sentence)
    first_char = ''
    if sentence == '':
        first_char = "None"
        return lng, first_char
    else:
        first_char = sentence[0]
        return lng, first_char
