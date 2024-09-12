#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary.items())
    for idx, (key, value) in enumerate(sorted_items):
        print("{}: {}".format(key, value))
