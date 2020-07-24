"""If condition in List comprehension"""

# numbers = list(range(1,11))
# nums_even = [i for i in numbers if i%2 == 0]
nums_even = [i for i in range(1,11) if i%2 == 0]
nums_odd = [i for i in range(1,11) if i%2 != 0]

# for i in numbers:
#     if i%2 == 0:
#         nums_even.append(i)
#     else:
#         nums_odd.append(i)

print(nums_even,nums_odd)