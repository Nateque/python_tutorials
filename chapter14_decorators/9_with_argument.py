"""Decorator with arguments"""

from functools import wraps

def check_datatype(datatype):
    def outer_func(function):
        @wraps(function)
        def inner_func(*args, **kwargs):
            if all([type(i) == datatype for i in args]):
                return function(*args, **kwargs)
            else:
                print("Wrong Input")
        return inner_func
    return outer_func

@check_datatype(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('nateq ','siddiqui', 4))