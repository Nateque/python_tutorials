"""Set comprehension"""

set1 = {i**2 for i in range(1,11)}
# print(set1)

names = ['nateq', 'siddiqui', 'mohd']
set2 = {name[0] for name in names}
# print(set2)