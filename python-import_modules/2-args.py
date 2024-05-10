#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print("Number of argument{}: {}{}".format('' if num_args == 1 else 's', num_args, '' if num_args == 0 else ':'))

    if num_args > 0:
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
    else:
        print(".")

