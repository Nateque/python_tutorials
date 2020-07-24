"""Function returning Function"""

def outer_func():
    def inner_func():
        print("Hello")
    return inner_func

var = outer_func()
# var()

def outer_func2(msg):
    def inner_func2():
        print(f"Message is : {msg}")
    return inner_func2

var2 = outer_func2('Hi there!')
# var2()