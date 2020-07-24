"""Raise errors """

def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('Wrong input')

print(add(5,'6'))