"""Iterator vs iterables"""

numbers = [1,2,3,4,5] # List, string, tuples, etc are "iterables"
nums = map(lambda a : a**2, numbers) # Iterator

# for i in numbers:
#     print(i)

# first iter function is call ---> iter(numbers) --> this is iterator
# then next function is call ---> next(iter(numbers))

# next_num = iter(numbers)
# print(next(next_num))
# print(next(next_num))
# print(next(next_num))
# print(next(next_num))