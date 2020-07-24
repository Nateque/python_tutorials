#Output
# you are calling add function
# docstring
# 9
from functools import wraps

def decorators(any):
    @wraps(any)
    def inner_deco(*args, **kwargs):
        '''This is inner deco'''
        print(f"you are calling '{any.__name__}' function")
        print(any.__doc__)
        return any(*args, **kwargs)
    return inner_deco

@decorators
def add(a,b):
    """This is add func"""
    return a**b

print(add(2,3))