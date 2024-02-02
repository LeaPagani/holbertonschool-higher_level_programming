#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'M' : 1000}
    result = 0
    previous = 0
    if type(roman_string) is str and roman_string:
        for iteration in roman_string:
            if roman_values[roman_string[iteration]] >= prev_value:
                result += roman_values[roman_string[iteration]]
            else:
                result -= roman_values[roman_string[iteration]]
            prev_value = roman_values[roman_string[iteration]]
    return result
