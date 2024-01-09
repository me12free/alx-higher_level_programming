#!/usr/bin/python3

def no_c(my_string):
    diction = {ord(char): None for char in "cC"}
    new_string = my_string.translate(diction)
    return new_string
