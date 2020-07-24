from csv import DictReader, DictWriter

with open('file1.csv', 'r') as rf:
    with open('final.csv', 'w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['name', 'email_id', 'phone_number'])
        csv_writer.writeheader()

        for row in csv_reader:
            name, email, phone = row['name'], row['mail'], row['phone']
            csv_writer.writerow({
                'name':name,
                'email_id':email,
                'phone_number':phone
            })