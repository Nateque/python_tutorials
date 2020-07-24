"""Dictionary Comprehension"""

# How to create key and its square value by dict compr
# You can use f string in this as well
# dict1 = {f"Square of {i}":i**2 for i in range(1,5)}
# print(dict1)
# for k,v in dict1.items():
    # print(f"{k} : {v}")

# Char count by dict compr
dict2 = 'natequesiddiqui'
count = {i:dict2.count(i) for i in dict2}
print(count)