# Special/ Magic/ Dunder method
# Operator Overloading
# Polymorphisom


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model} {self.price}"

    # __str__, __repr__
    def __str__(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    def __repr__(self):
        return f"Phone (\'{self.brand}\', \'{self.model}\', {self.price})"

    def __len__(self):
        return len(self.phone_name())

    # Operator Overloading
    def __add__(self, other):
        return self.price + other.price

p1 = Phone('mi', 'note3', 12000)
p2 = Phone('mi', 'note4', 16000)
print(p1 + p2)

# print(len(p1))
# print(repr(p1))
# print(p1.phone_name())

