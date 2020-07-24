# we use OS Module to handle our OS like creating files, folders, etc

import os

# print(os.getcwd())
# os.chdir(r'D:\python_tutorials')
# os.mkdir('New Folder')
# print(os.path.exists('New Folder'))
# open('new file', 'a').close()
# print(os.listdir())

for item in os.listdir():
    path = os.path.join(os.getcwd(), item) # it will print with full path
    print(path)

# for item in os.listdir(r'D:\python_tutorials'):
#     path = os.path.join(r'D:\python_tutorials', item) # it will print with full path
#     print(path)