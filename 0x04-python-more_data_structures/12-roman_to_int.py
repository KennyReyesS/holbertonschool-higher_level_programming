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
        'M': 1000
}
    for i in range(len(roman_string)):
        for key in d_roman:
            if roman_string[i] == key:
                new_list.append(d_roman[key])
    suma = sum(new_list)
    return (suma)
