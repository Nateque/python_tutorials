"""More important things about list"""

# Range in list
# numbers = list(range(1,11))
# print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 4,  7, 8, 9, 10]
# Pop Value
# popped_item = numbers.pop() # When you use popped method it will still store last value which you popped.
# print(popped_item)

# Index in list
print(numbers.index(4, 4, 8)) # it will tell the position of value, # from where till where

# Pass list to a function
# def negative_function(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative

# print(negative_function(numbers))