"""Update method in dict"""

user_info = {
    'name' : 'nateq',
    'age' : 23,
    'colony' : 'arif'
}

more_info = {
    'name' : 'nateq siddiqui',
    'gender' : 'male'
}
user_info.update(more_info) # It will update data and if not present it will add it
print(user_info)