#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a, b = 10, 5

if __name__ == "__main__":
    results = {
        "Addition": add(a, b),
        "Subtraction": sub(a, b),
        "Multiplication": mul(a, b),
        "Division": div(a, b)
    }

    for operation, result in results.items():
        print(f"{a} {'+' if operation == 'Addition' else '-' if operation == 'Subtraction' else '*' if operation == 'Multiplication' else '/'} {b} = {result}")
