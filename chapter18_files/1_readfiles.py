""" readfile
    tell method - tell us cursor position
    seek method - change cursor position
    readline - print only 1 line
    readlines - make list of all lines from file """

# f = open('txt1.txt') # openfile
# print(f'cursor position - {f.tell()}') #tell method
# print(f.read()) # read method 
# f.seek(0) # seek method
# print(f.read())
# f.close() # close file

# f = open('txt1.txt') # openfile
# # print(f.readline(), end='') # readline method
# # print(f.readline(), end='') 
# # lines = f.readlines() # readlines method
# # print(lines)
# # print(f.name) # print file name
# # print(f.closed) # check file closed or not
# f.close() # close file

# f = open(r"D:\python_tutorials\txt1.txt")

# for i in f.readlines()[:1]:
#     print(i, end='')

# f.close()

""" With Block - context manager"""

with open('txt1.txt') as f:
    print(f.read())

print(f.closed)