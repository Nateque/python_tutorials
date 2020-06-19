# Whenever you return 2 or more values from functions it will return it as a tuple

def sum_fun(int1,int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(type(sum_fun(2,4)))

# You should assign values to different vars

a, b = sum_fun(2,4)
print(a,b)