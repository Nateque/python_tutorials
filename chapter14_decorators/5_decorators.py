"""Decorators part 2"""

from functools import wraps # Import Wraps func
def decorators_func(funcs):
    @wraps(funcs) # Use Wraps func
    def decorators(*args, **kwargs):
        """This is decorators"""
        print("This func do calculations")
        return funcs(*args, **kwargs)
    return decorators

@decorators_func
def func1(a,b):
    """This is func1 """
    return a**b
# print(func1(5,2))

print(func1.__doc__)
print(func1.__name__)