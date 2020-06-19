# Sum of each number given by user using for loop

num = input("Enter more than one digit number: ")

total = 0
for i in range(len(num)):
    total += int(num[i])

print(f"Sum of {num} is {total}")