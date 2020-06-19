# More about tuples

# You can write without parenthesis
mixed = 1,2,3,4,5.0
# print(type(mixed))

# Loops in tuples
# for i in mixed: # You can use while loop as well
    # print(i) 

# tuple with 1 element
one = 1, # for one element in tuple you have to write , in last
words = 'mango',
# print(type(words))

# Tuples unpacking
cricketers = 'sachin', 'dhoni', 'virat'
cricketer1, cricketer2, cricketer3 = cricketers
# print(cricketer3)

# List inside tuples
favourites = (1,2,4, [5,6,7,8], 9,10)
# favourites[3].pop()
# favourites[3].append(8)
# print(favourites)

# min, mix and sum functions
# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))
