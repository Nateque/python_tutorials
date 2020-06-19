# Define a function to return a dict of cube of every number

def cube_dic(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube

num = int(input("enter any number : "))
print(f"Cube of your number {cube_dic(num)}")