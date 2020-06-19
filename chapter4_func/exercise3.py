# Check name is palindrome or not by defining function

# Method 1
def is_palindrome(name):
    if name==name[::-1]:
        return "Palindrome"
    return "Not Palindrome"

uname = input("Enter your name: ")
print(f"Your name {uname} is {is_palindrome(uname)}")

# #Method 2
# def is_palindrome(name):
#     return name == name[::-1] # It will return value in True or False (Boolean)
 
# uname = input("Enter your name: ")
# print(f"{is_palindrome(uname)}")