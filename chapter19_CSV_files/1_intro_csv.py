# CSV - Comma seprated values
from csv import reader

# with open('file1.csv', 'r') as f:
#     csv_reader = reader(f) #iterator values
#     next(csv_reader) # if you want to skip first values
#     for row in csv_reader:
#         print(row)

# using DictReader to read csv files

from csv import DictReader
# ordered dictionary

with open('file1.csv', 'r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row['mail'])