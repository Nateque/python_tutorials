"""Generator comprehension and time consumption"""
import time

# To create list comprehension
# l = [i**2 for i in range(1,11)]
# print(l)

# To create generator comprehension
l = (i**2 for i in range(1,11)) # You just have to write in brackets
# print(l)


"""How much time both takes"""


# To create list comprehension
t1 = time.time()
l = [i**2 for i in range(1,10000000)]
print(time.time() - t1)

# To create generator comprehension
t2 = time.time()
l = (i**2 for i in range(1,10000000)) # You just have to write in brackets
print(time.time() - t2)
# print(l)