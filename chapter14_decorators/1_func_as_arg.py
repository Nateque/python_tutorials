"""Function as a argument"""

# def square(n):
#     return n**2

lists = [1,2,3,4,5]

# print(list(map(lambda a: a**2, lists)))

"""Now we will create our own map function"""

# def my_map(func, l):
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list

# By list compr
def my_map2(func, l):
    return [func(i) for i in l]

print(my_map2(lambda a : a**3, lists))