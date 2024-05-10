#!/usr/bin/python3
a = 1
b = 2

add_0_module = __import__('add_0')
add = add_0_module.add

result = add(a, b)
print("{} + {} = {}".format(a, b, result))
