# Ask user to input more than one digit number and calculate sum of each digit

unum = input("Enter more than one digit : ")

total = 0
i = 0
while i < len(unum):
    total += int(unum[i])
    i += 1

print(f"Sum of your {unum} is {total}")