"""Introduction to * args"""
"""It is like flexible function"""

# def sums(a,b): # In this if you pass more or less values than 2 it will give errors
#     return a+b
# print(f"{sums(4,4)}")

def total(*args): # You can pass many args by using *args, it will get in list as a Tuple 
    total = 0
    for num in args:
        total += num
    return total

# print(f"{total(1,2,3,4,5)}")