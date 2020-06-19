# Looping and in keyword in dictionary

user_info = {
    'name' : 'nateq',
    'age' : 23,
    'fav_movies' : ['ff', 'hp', 'eg'],
    'fav_series' : ['mn', 'bb']
}

# How to check key present or not in dict
# if 'names' in user_info:
#     print('present')
# else:
#     print('not present')

# How to check value present or not in dict
# if 23 in user_info.values():
#     print('present')
# else:
#     print('not present')

"""Looping in dict"""
# How to print keys
# for i in user_info: # You can add .keys() method for key but it is by default
#     print(i)

# how to print values
# for i in user_info.values():
#     print(i)
# # OR
# for i in user_info:
#     print(user_info[i])

# .items() method 
# user_items = user_info.items()
# print(type(user_items))

# for i, j in user_info.items():
#     print(f"Value of {i} key is {j}")
