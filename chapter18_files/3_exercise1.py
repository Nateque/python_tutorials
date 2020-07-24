# copy data from file2 and print it in a good manner

with open('file2.txt', 'r') as rf:
    with open('output.txt', 'a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name}\'s salary is {salary}")