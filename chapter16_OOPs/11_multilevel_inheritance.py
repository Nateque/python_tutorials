"""Multilevel Inheritance, Method resolution order"""

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model}"
        # and lastly this method if not found any methods in class smartphone and smartphone2

class Smartphone(Phone):
    def __init__(self, brand, model, price, camera, ram):
        super().__init__(brand, model, price)
        self.camera = camera
        self.ram = ram

    def full_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"
        # and if not found in smartphone2 class python will call this method

class Smartphone2(Smartphone):
    def __init__(self, brand, model, price, camera, ram, processor):
        super().__init__(brand, model, price, camera, ram)
        self.processor = processor

    def full_name(self):
        return f"{self.brand} {self.model} and price & ram is {self.price} & {self.ram}"
        # according to MRO, python first call this method

p1 = Phone('mi','note3',12000)
s1 = Smartphone('redmi','note7',18000,'12px','4gb')
s2 = Smartphone2('redmi','note9',28000,'18px','8gb', 12)

# print(s1.full_name() + f"and price is {s1.price}")
# print(s2.full_name() + f" and price & ram is {s2.price} & {s2.ram}")
# print(s2.full_name())
# print(help(Smartphone2))

# print(isinstance(s2, Phone)) 
# print(issubclass(Smartphone2, Phone))