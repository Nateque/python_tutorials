"""Character counter programm using Dict"""

uname = input("Enter your name : ")

def char_count(n):
    count = {}
    for char in n:
        count[char] = n.count(char)
    return count

print(char_count(uname))