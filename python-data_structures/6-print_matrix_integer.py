#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for char in row:
            print("{:d}".format(char), end="")
            if char != row[-1]:
                print(" ", end="")
        print("")
