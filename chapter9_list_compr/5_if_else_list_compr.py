"""If Else Nested in List Comprehension"""

# def if_else(l):
#     return [i*2 if i%2 == 0 else -i for i in l]

# print(f"{if_else(range(1,11))}")

# How to create this type of list = [[1,2,3],[1,2,3],[1,2,3]] by List comp
mixed = [[i for i in range(1,4)] for j in range(0,3)]
# print(mixed)