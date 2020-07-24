"""Define a function and pass 2 values, 1st as a normal parameter and 2nd as *args, 
and multiply *args values by normal parameter"""

def multiply_fun(num, *args):
    if args:
        return [num**i for i in args]
    else:
        return 'You didn\'t enter anything'

nums = [3,4,5,6]
print(multiply_fun(2, *nums))