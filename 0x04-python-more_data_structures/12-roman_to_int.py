#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return (0)
    new_list = []
    d_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and \
           d_roman[roman_string[i]] < d_roman[roman_string[i + 1]]:
            num = num - d_roman[roman_string[i]]
        else:
            num = num + d_roman[roman_string[i]]
    return (num)
