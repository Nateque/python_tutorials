"""Filter Function"""

numbers = [2,3,4,1,4,5,7,4,5,8,3]

evenss = [i for i in numbers if i%2 == 0]
# print(evenss)

# def is_even(n):
#     return n%2 == 0

odds = tuple(filter(lambda a : a%2==1 ,numbers))
print(odds)