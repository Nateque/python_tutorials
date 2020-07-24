"""What is class variable"""

class Circle:
    pie = 3.14 # Class Var
    def __init__(self, radius):
        self.radius = radius
    
    def calc_circumstances(self):
        return 2*Circle.pie*self.radius # For constant class var use 'ClassName.Value'

c = Circle(4)
print(c.calc_circumstances())

# Example 2

class Laptop:
    discount_percent = 10 # Class Var
    def __init__(self, brand_name, model, price):
        self.brand = brand_name
        self.model = model
        self.price = price
        self.name = brand_name + ' ' + model

    def discount(self):
        value = (self.price / 100) * self.discount_percent # Always use 'Self' for class var so you can change sometimes
        return self.price - value

l1 = Laptop('HP', 'Core i3', 63000)
l2 = Laptop('Dell', 'Core i5', 44000)
# Laptop.discount_percent = 30
# print(l2.discount())