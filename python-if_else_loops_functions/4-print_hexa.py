#!/usr/bin/python3

for i in range(99):
    print("{} = {}".format(i, hex(i)), end="\n" if i % 10 == 9 else " ")
