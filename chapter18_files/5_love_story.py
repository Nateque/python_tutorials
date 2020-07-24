with open('read.txt', 'r', encoding='utf-8') as f:
    # print(f.encoding)
    data = f.read(100)
    # print(data)
    while len(data) > 0:
        print(data)
        data = f.read(100)
