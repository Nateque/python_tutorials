"""What is List comprehension?"""

# Normal Way to create square list 
squares = []
for i in range(1,11):
    squares.append(i**2)
# print(squares)

# By using List Comprehension
squares2 = [i**2 for i in range(1,11)]
# print(squares2)

# Normal way to create Negative List
negative_list = []
for i in range(1,11):
    negative_list.append(-i)
# print(negative_list)

# By using List comprehension
negative_list2 = [-i for i in range(1,11)]
# print(negative_list2)

# First char of list values in another list
names = ['nateq', 'siddiqui', 'ahmed', 'asef']
# names2 = []
# for i in names:
#     names2.append(i[0])
names2 = [i[0] for i in names]
# print(names2)
