"""Defin instance method to calculate discount in class Laptop"""

class Laptop:
    def __init__(self, brand_name, model, price):
        self.brand = brand_name
        self.model = model
        self.price = price
        self.name = brand_name + ' ' + model

    def discount(self, n1):
        value = (self.price / 100) * n1
        return self.price - value

l1 = Laptop('HP', 'Core i3', 63000)
l2 = Laptop('Dell', 'Core i5', 44000)

# print(l1.name)
# print(l2.name)

print(l1.discount(10))