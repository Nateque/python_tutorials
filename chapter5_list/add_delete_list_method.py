"""Methods to add Data in list"""

# 1.Append Method - It will add in last 
# fruits1 = ['mango', 'apple']
# fruits.append('Banana')
# print(fruits)

# 2.Insert method - It will add in the given position
# fruits1.insert(1,"Banana")
# print(fruits1)

# 3.Extend method - It will extend 2nd list in to 1st list
# fruits2 = ['banana', 'orange']
# fruits = fruits1 + fruits2 #Normal method
# print(fruits)
# fruits1.extend(fruits2) # Extend method
# print(fruits1)

# Difference between extend and append method
# fruits1.append(fruits2) # It will direct add as a list 
# print(fruits1)

"""Methods to delete Data from List"""

# 1.Pop method - It will delete the last value
fruits1 = ['mango', 'apple', 'kiwi', 'orange']
# fruits1.pop(1) # if we dont give any position it will delete last one 
# print(fruits1)

# 2.Del Statement
# del fruits1[1] # it will delete the given position value, it will give error if we dont give any position
# print(fruits1)

# # 3.Remove Method
# fruits1.remove('kiwi') # we have to give value not position to delete entry from the list
# print(fruits1) # if we give 2 values it will simply delete 1st one
