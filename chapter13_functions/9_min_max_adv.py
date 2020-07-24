"""Max and Min Function advance use"""

names = ['nateque', 'nateq', 'siddiqui']

# print(max(names, key=lambda a: len(a)))

students = [
    {'name': 'nateq', 'score':99, 'age':23},
    {'name': 'ahmed', 'score':95, 'age':25},
    {'name': 'asef', 'score':90, 'age':22}
]

# print(max(students, key= lambda item:item.get('score'))['name'])

students2 = {
    'nateque' : {'score':99,'age':23},
    'ahmed' : {'score':95,'age':25},
    'asef' : {'score':90,'age':22}
}

a = lambda item: students2[item]['score']
# print(max(students2, key= a))