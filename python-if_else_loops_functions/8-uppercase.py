#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()

uppercase("best")
uppercase("Best School 98 Battery street")
