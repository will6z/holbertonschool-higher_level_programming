#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    import calculator_1

    result_add = calculator_1.add(a, b)
    result_subtract = calculator_1.subtract(a, b)
    result_multiply = calculator_1.multiply(a, b)
    result_divide = calculator_1.divide(a, b)

    print("Addition result:", result_add)
    print("Subtraction result:", result_subtract)
    print("Multiplication result:", result_multiply)
    print("Division result:", result_divide)
