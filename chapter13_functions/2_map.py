"""Map Function"""

numbers = [1,2,3,4,5]
# normal func way
# def squares(n):
#     return [i**2 for i in n]

# Map Func
squaress = list(map(lambda a: a**2, numbers))
# print(squaress)

names = ['nateq', 'siddiqui', 'harshit']
# Normal way
# def func(n):
#     list_pos = []
#     for i in names:
#         list_pos.append(len(i))
#     return list_pos
# print(f"{func(names)}")

# List compr
# def funcs(n):
#     return [len(i) for i in n]
# print(f"{funcs(names)}")

# Map func
length = list(map(len, names)) # because LEN is already a function
print(length)