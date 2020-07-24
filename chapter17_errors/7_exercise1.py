# defin a function and use try except

def divide(a,b):
    try:
        return a/b
        
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    # else:
    #     # return a/b


print(divide(2,'2'))