#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    for idx in range(len(nlist)):
        if nlist[idx] == search:
            nlist[idx] = replace
    return nlist
