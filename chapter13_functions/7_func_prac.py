"""Adv. Function practice"""

# By Normal func
# def average_fun(*args):
#     average = []
#     for i in zip(*args):
#         average.append(sum(i)/len(i))
#     return average

# By List compr
# def average_fun(*args):
#     return [sum(i)/len(i) for i in zip(*args)]

# By Lambda Func
lists = lambda *args: [sum(i)/len(i) for i in zip(*args)]

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
# print(lists(l1,l2,l3))


"""More Practice"""

roll_no = [1,2,3,4]
maths = [100,90,80,70]
science = [90,67,88,80]
english = [78,99,78,67]
bio = [55,78,80,88]
geo = [78,88,87,66]

# def percentage(*args):
#     percent = []
#     for i in zip(*args):
#         percent.append(sum(i)/len(i*100))
#     return percent

percentage = lambda *args: [round((sum(i)/(len(i)*100))*100, 1) for i in zip(*args)]

# Round function use to round the figure 
print(percentage(maths, science, english, bio, geo))