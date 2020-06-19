"""Difference between LIST and STRING"""

# Strings are immutable - means you cannot change it
name = 'nateq'
name.title() # it will not change because strings are immutable
print(name)

# List are mutable - you can change lists
list1 = ['item1', 'item2', 'item3']
list1.append('item4') # it will append because lists are mutable
print(list1)