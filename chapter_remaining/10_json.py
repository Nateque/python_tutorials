import json

data = '{"nateq":"siddiqui", "age": 24}'
print(data)
print(type(data))

parsed = json.loads(data)
print(parsed['age'])
print(type(parsed))

data2 = {
    'name' : 'nateq',
    'hobbies' : ['football', 'coding', 'comedy'],
    'friends' : ('ahmed', 'asef')
}

print(data2)
jscomp = json.dumps(data2)
print(jscomp)