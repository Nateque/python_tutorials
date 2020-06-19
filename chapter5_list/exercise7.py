# Define a function to print how many sublists are in a list

lists = [1,2,3,[1,2], [4,5,6], 7,8,9, [12,44,55]]

def sublist_fun(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

print(f"There are {sublist_fun(lists)}")