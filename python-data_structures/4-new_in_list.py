#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        return None
    copy = [x for x in my_list]
    copy[idx] = element
    return copy
