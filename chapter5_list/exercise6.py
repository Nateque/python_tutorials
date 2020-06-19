# Find greatest difference by using MIN and MAX Functions

numbers = [6,33,66,44,99,44]
# print(min(numbers))
# print(max(numbers))

def min_max(l):
    return max(l) - min(l)

print(min_max(numbers))