"""Decorators Intro"""


def deco_func(func):
    def decorator():
        print('This func is amazing')
        func()
    return decorator

@deco_func # Shortcut to call Decorator
def func1():
    print('This is function 1')
func1()

@deco_func # Shortcut to call Decorator
def func2():
    print('This is function 2')
func2()


# var = deco_func(func2)
# var()