# writer # DictWriter

from csv import writer

with open('file2.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['nateq','india'])
    # csv_writer.writerow(['ahmed','india'])
    csv_writer.writerows([['name','country'],['nateq','india'],['ahmed','india']])

from csv import DictReader

with open('file2.csv', 'r') as rf:
    csv_reader = DictReader(rf)
    for row in csv_reader:
        print(row)