# Take name of user and print how many times each characters are present in name

uname = input("Enter you name : ")

temp = ""
i = 0
while i < len(uname):
    if uname[i] not in temp:
        temp += uname[i]
        print(f"{uname[i]} : {uname.count(uname[i])}")
    i += 1