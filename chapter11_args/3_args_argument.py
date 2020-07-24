"""args as a argument"""

def multiply_fun(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

nums = [1,2,3,4,5,6,7]
print(f"{multiply_fun(*nums)}") # It will unpack this list