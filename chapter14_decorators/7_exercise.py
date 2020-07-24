"""Define a function to calculate time using decorator"""

import time

def calc_time(any):
    def time_inner(*args, **kwargs):
        t1 = time.time()
        any_value = any(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)
        return any_value
    return time_inner

@calc_time
def fun1(n):
    return [i**3 for i in (range(1,n+1))]

fun1(1000)