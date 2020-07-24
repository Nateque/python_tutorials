# DictWriter
from csv import DictWriter

with open('file3.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['name','mail','age'])
    csv_writer.writeheader()
    # writerow, writerows
    # csv_writer.writerow({
    #     'name':'nateq',
    #     'mail':'nateq@gmail.com',
    #     'age' : 24
    # })
    # csv_writer.writerow({
    #     'name':'ahmed',
    #     'mail':'ahmed@gmail.com',
    #     'age' : 26
    # })

    # writerows ---> [dict, dict, dict]
    csv_writer.writerows([
        {'name':'nateq','mail':'nateq@gmail.com','age':23},
        {'name':'ahmed','mail':'ahmed@gmail.com','age':25},
        {'name':'asef','mail':'asef@gmail.com','age':23}
    ])