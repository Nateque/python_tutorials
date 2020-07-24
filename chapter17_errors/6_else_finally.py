# Try except Else Finally

while True:
    try:
        age = int(input('Enter age :'))
    except ValueError:
        print('Enter correct age')
    except:
        print('unexpected error')
    else:
        print(f'you entered {age}')
        break
    finally:
        print('finally block...')