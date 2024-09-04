#!/usr/bin/python3
hex_numbers = ""
for number in range(0, 99):
    hex_number = hex(number)
    hex_numbers += f"{number} = {hex_number}\n"
print("{}".format(hex_numbers.strip()))
