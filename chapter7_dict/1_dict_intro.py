"""Introduction to Dictionary in Python"""

# There are 2 ways to create dictionaries
# 1st method
user = {'name' : 'nateq', 'age' : 23}
# 2nd method
user2 = dict(name = 'nateq', age = 23)
# print(user2)

# How to access Dictionary values
# print(user2['name'])

# How to create dictionary in easy syntax

user_info = {
    'name' : 'siddiqui',
    'age' : 23,
    'fav_movies' : ['ff', 'avengers'],
    'fav_series' : ['mh', 'bb']
}

# print(user_info['fav_movies'])

# Dictionary into dictionary


user_info2 = {
    'user_info' : {
    'name' : 'siddiqui',
    'age' : 23,
    'fav_movies' : ['ff', 'avengers'],
    'fav_series' : ['mh', 'bb']
}
}
# print(user_info2)

# How to add data in dictionary

user_info3 = {}
user_info3['name'] = 'nateq'
user_info3['age'] = 24
# print(user_info3)