#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    count = len(sys.argv) - 1
    for i in range(1, count + 1):
        if count == 0:
            continue
        result += int(sys.argv[i])
    print(result)
