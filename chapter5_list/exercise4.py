# Filter odd even from list by defining function

numbers = list(range(1,21))

def odd_even(l):
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [odd, even]

print(f"Filtered list : {odd_even(numbers)}")