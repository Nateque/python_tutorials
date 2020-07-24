"""Enumerate function"""

# Normal way
names = ['abc', 'pqr','siddiqui', 'nateq']

# pos = 0
# for name in names:
#     print(f"{pos} ----> {name}")
#     pos += 1

# Enumerate func
# for pos, name in enumerate(names):
    # print(f"{pos} ----> {name}")

def func(n,l):
    for pos, name in enumerate(l):
        if name == n:
            return pos
    return "Not Found!"

print(f"{'nateq'} --> {func('nateq',names)}")