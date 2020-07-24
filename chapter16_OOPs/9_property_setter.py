"""we will see how to solve 3 small problems like negative value in object etc"""

class Phone:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self._price = max(price, 0) # if price is less than zero it will print zero #Small trick
        # self.full_details = f"{name} {model} and price is {price}" # it will not chane if we give input from outside class

    @property #after calling this you dont have to call your function as a function
    def full_details(self):
        return f"{self.name} {self.model} and price is {self._price}"

    @property
    def price(self): 
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

p1 = Phone('mi', 'note3', 12000)
p1.price = -9000

print(p1.full_details) # Now after calling property you can write without parenthesis 

