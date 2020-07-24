"""Intersection, Union, Loop and IN keyword in Sets"""

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

s = s1 & s2 # Intersection symbol is "&" 
s = s1 | s2 # Union symbol is "|"
# print(s)

# if 2 in s1: # IN Keyword in sets
#     print("Present")
# else:
#     print("Not present")

for item in s1: # For loop in sets
    print(item)