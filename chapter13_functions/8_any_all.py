"""Any and All func"""

num1 = [2,3,6,8]
num2 = [1,3,6,7]

even_check = all([i%2==0 for i in num1]) # Short of [True if i%2==0 else False for i in num1]
# print(even_check)
odd_check = any([i%2==0 for i in num2])
# print(odd_check)

"""Practice Any and All"""

def func(*args):
    lists = [type(i) == int or type(i) == float for i in args]
    if all(lists) == True:
        total = 0
        for i in args:
            total += i
        return total
    return 'Wrong Input'


print(func(1,2,3,4.5,'sidd'))