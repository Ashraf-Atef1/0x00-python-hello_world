#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_symbol = {"M": 1000, "D": 500,
                    "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    if roman_string and roman_string is str:
        old_value = 0
        for char in roman_string:
            if old_value < roman_symbol[char]:
                sum += roman_symbol[char] - old_value * 2
            else:
                sum += roman_symbol[char]
            old_value = roman_symbol[char]
    return sum
