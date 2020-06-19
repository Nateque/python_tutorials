"""Reversed the text of each entry of list"""

words = ['abc', 'pqr', 'xyz', 'nop']

def reverse_fun(l):
    reverse = []
    for i in l:
        reverse.append(i[::-1])
    return reverse

print(f"Reversed list {reverse_fun(words)}")