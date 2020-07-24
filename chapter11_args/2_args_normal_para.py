""" *args with normal parameter"""

def multiply_fun(num, *args): # If you write normal parameter then first value will be normal and others tuple
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(f"{multiply_fun(2,2,3,4)}")