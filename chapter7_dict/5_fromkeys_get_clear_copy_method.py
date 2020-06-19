""" Fromkeys, get, copy, clear methods in dict""" 

# user_info = dict.fromkeys(['name','age','height'], 'unknown')
# print(user_info)
# it will create : {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

user_info = {'name': 'nateq', 'age': 34, 'age': 24} # if we use double key, it will only write last one
print(user_info)

# Get method
# print(user_info.get('name'))
# print(user_info.get('names','not found!'))


# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')
    
# if user_info.get('names'):
#     print('present')
# else:
#     print('not present')

# To clear dict
# user_info.clear()
# print(user_info)

# Copy method
# d = user_info.copy()
# print(d)
