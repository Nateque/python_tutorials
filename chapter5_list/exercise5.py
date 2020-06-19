# Define a function and print same elements of list by passing two lists in functions

number1 = [1,2,3,4,7]
number2 = [4,5,2,6,7]

def same_fun(l1,l2):
    same = []
    for i in l1:
        if i in l2:
            same.append(i)
    return same

print(f"Same number: {same_fun(number1,number2)}")