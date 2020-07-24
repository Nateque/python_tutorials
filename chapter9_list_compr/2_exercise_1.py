"""Define a function to reversed the list alphabets by List Compr"""

# Normal way
# names = ['name1', 'name2', 'name3']
# def revers_list(l):
#     revers = []
#     for i in l:
#         revers.append(i[::-1])
#     return revers
# print(f"Reversed of list : {revers_list(names)}")

# By using List comprehension
names = ['name1', 'name2', 'name3']

def revers_list(l):
    return [i[::-1] for i in l]
print(f"Reversed of list : {revers_list(names)}")
