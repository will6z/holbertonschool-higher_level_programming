#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()

    for num in my_list:
        unique_integers.add(num)

    sum_unique = sum(unique_integers)
    return sum_unique
