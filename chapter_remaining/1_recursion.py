# Recursion - function inside function

# factorial = 5 * 4 * 3 * 2 * 1

# def fact(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#         # 1 = 1 * (1)
#         # 1 = 1 * (2)
#         # 2 = 2 * (3)
#         # 6 = 6 * (4)
#     return fac
# print(fact(5))

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# fabinacco = 0 1 1 2 3 5 8 13 

def fabinacco(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fabinacco(n-1) + fabinacco(n-2) #(n-1) + n

print(fabinacco(9))