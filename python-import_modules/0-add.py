#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2

    import_module = __import__('add_0')
    add = import_module.add

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
