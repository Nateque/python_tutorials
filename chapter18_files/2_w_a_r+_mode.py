# w - Write mode
# a - append mode
# r+ - read and write mode

# with open('txt1.txt', 'w') as f:
#     f.write('Hello, how are you?\n')

# with open('txt1.txt', 'a') as f:
#     f.write('i am fine\n')

# with open('txt1.txt', 'r+') as f:
#     f.seek(len(f.read()))
#     f.write('good\n')

# how to write from one file to another

with open('file2.txt', 'r') as rf:
    with open('file1.txt', 'w') as wf:
        wf.write(rf.read())