#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        for index in my_list[::-1]:
            print("{:d}".format(index))
