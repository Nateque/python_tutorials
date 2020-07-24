"""Pass a list in function and return with first capital word and reverse if written using kwargs """

names = ['nateq','siddiqui','ahmed','asef']

def func(name, **kwargs):
    if kwargs.get('reverse') == True:
        return [i[::-1].title() for i in name]
    else:
        return [i.title() for i in name]

print(f"{func(names, reverse = True)}")