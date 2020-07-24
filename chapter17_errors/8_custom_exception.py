# how to create custom exception

class NameToShortError(ValueError):
    pass

def check(name):
    if len(name) < 8:
        raise NameToShortError('you enter short name...')
    else:
        print(f'Hello {name}')

name1 = input('Enter your name: ')
print(check(name1))