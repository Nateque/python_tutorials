"""Decorator allow to take only int values """

from functools import wraps

def only_int(function):
    def int_inner(*args,**kwargs):
        if all([type(i)==int for i in args]):
            return function(*args,**kwargs)
        else:
            print("wrong input")
        # datatypes = []
        # for i in args:
        #     datatypes.append(type(i) == int)
        # if all(datatypes):
        #     return function(*args, **kwargs)
        # else:
        #     print("Wrong input")
    return int_inner

@only_int
def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(1,2,3,4,5,'nice'))