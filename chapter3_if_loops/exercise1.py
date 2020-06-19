# Guess number by taking one number from user without loop.

unum = int(input("Enter your number: "))
winning_num = 5
if unum == winning_num:
    print("You won! Congrats")
else:
    if unum < winning_num:
        print("Increase number")
    else:
        print("Decrease number")

