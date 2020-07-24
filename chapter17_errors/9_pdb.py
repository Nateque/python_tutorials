# debugging in python 

import pdb

pdb.set_trace()
# l - line number
# c - continue
# q - quit
# n - next line

name = input('Enter your name: ')
age = input('Enter your age: ')
age2 = int(age) + 5
print(f"Hi {name}, you will be {age2} after five years")