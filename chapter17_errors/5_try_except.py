# exception handling
# Try except else finally

while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('invalid input...')
    except:
        print('unexpected error')

if age > 18:
    print('You can play this game')
else:
    print('You can\'t play')