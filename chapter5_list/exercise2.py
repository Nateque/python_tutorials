# Define a function to reverse list by using pop and append method

list1 = list(range(1,21))

def reverse_fun(l):
    reverse = []
    for i in range(len(l)):
        reverse.append(l.pop())
    return reverse

print(f"Reversed list {reverse_fun(list1)}")