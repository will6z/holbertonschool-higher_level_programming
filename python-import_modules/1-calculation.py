#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    import calculator_1 as calc
    
    result_add = calc.add(a, b)
    result_subtract = calc.subtract(a, b)
    result_multiply = calc.multiply(a, b)
    result_divide = calc.divide(a, b)
    
    print("Addition: {} + {} = {}, Subtraction: {} - {} = {}, Multiplication: {} * {} = {}, Division: {} / {} = {}".format(a, b, result_add, a, b, result_subtract, a, b, result_multiply, a, b, result_divide))
