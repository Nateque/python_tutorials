"""Create a Laptop class with attributes like brand name, model, price
create two objects/instance of your laptop class"""

class Laptop:
    def __init__(self, brand_name, model, price):
        self.brand = brand_name
        self.model = model
        self.price = price
        self.name = brand_name + ' ' + model

l1 = Laptop('HP', 'Core i3', 34000)
l2 = Laptop('Dell', 'Core i5', 44000)

print(l1.name)
print(l2.name)