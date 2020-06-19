"""How to add and delete in dict"""

user_info = {
    'name' : 'nateque',
    'age' : 23,
    'fav_movies' : ['hp', 'ff', 'eg'],
    'fav_series' : ['mh','bb']
}

# How to add
user_info['fav_name'] = 'nateq'
# print(user_info)

# how to pop
# popped_item = user_info.pop('fav_name') # if you dont pass any argument in pop method it will give error
# print(f"Popped item is \'{popped_item}\'") 

# popitem
# popped_item = user_info.popitem()
# popped_item2 = user_info.popitem()
# popped_item3 = user_info.popitem()
# print(type(popped_item))
# print(popped_item3)