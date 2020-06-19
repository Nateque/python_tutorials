"""Create empty dict and take inputs from user and add it in dict"""

# user = {}

# name = input("Enter your name : ")
# age = input("Enter your age : ")
# fav_mov = input("Add Fav movies seprated by \",\" : ").split(",")
# fav_songs = input("Add Fav songs seprated by \",\" : ").split(",")

# user['name'] = name
# user['age'] = age
# user['fav_mov'] = fav_mov
# user['fav_songs'] = fav_songs

# for key, values in user.items():
#     print(f"{key} : {values}")


# Another short method

user = dict.fromkeys(['name', 'age', 'fav_mov', 'fav_songs'], 'unknown')

for i in user:
    user[i] = input(f"Enter your {i}, seprated by commas : ").replace(" ","").split(",")

for k,v in user.items():
    print(f"{k} : {v}")