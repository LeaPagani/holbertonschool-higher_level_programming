#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ldigit = -number % 10
        ldigit = -ldigit
    elif number > 0:
        ldigit = number % 10
    else:
        ldigit = 0
print(ldigit, end="")
