# Print square list of list numbers by using in functions

list1 = list(range(1,11))

def square_fun(l):
    square = []
    for i in l:
        square.append(i*i)
    return square

print(f"Square of {list1} is {square_fun(list1)}")