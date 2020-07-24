"""Pass a list in function and return only int and float values as a string"""

list1 = ['name', 1, 2, 3.3, [1,2,3], True, False]

# def output1(l):
#     output_list = []
#     for i in l:
#         if type(i) == int or type(i) == float:
#             output_list.append(str(i))
#     return output_list

def output2(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]

print(f"Output of list : {output2(list1)}")