"""Adv. practice of Sorted function"""

bikes = [
    {'model':'splender', 'price':34000},
    {'model':'yamaha', 'price':24000},
    {'model':'pulser', 'price':44000}
]

sorted_bikes = sorted(bikes, key= lambda item : item['price'], reverse= True)
print(sorted_bikes)