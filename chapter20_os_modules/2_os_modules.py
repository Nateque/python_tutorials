# OS Module part 2

import os

# print(os.listdir())
# os.mkdir('folder2')
# os.makedirs('new/new2/new3') # create multiple folders
# open(r'D:\python_tutorials\chapter20_os_modules\folder\new1', 'a').close()

# path = os.walk(os.getcwd())

# for current_path, folder_name, file_name in path:
#     print(f'current path : {current_path}')
#     print(f'folder name : {folder_name}')
#     print(f'file name : {file_name}')


# shutil module

import shutil

# os.rmdir('new') # it will only delete empty directory

# shutil.rmtree('new') # it will completely delete
# shutil.copy('file.txt', 'new/file.txt') # it will copy file
# shutil.copytree('new', 'new1/new') # it will copy folder
# shutil.move('file.txt', 'new1/new_file.txt') 