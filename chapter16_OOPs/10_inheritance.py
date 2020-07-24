"""Intro to inheritance"""

class Phone: # Base / Parent class
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self._price = max(price,0)

    def full_name(self):
        return f"{self.name} {self.model}"

    def make_call(self, number):
        return f"Calling {number} ....."

class Smartphone(Phone): # Derived / child Class
    def __init__(self, name, model, price, camera, ram):
        #two ways
        # Phone.__init__(self, name, model, price) # Uncommon way

        super().__init__(name, model, price) # Mostly we use this
        self.camera = camera
        self.ram = ram



    
p1 = Phone('mi','note3',-12000)
s1 = Smartphone('redmi','note7',18000,'12px','6gb')

print(s1.full_name() + f"and price is {s1._price}")
# print(p1.make_call(8956165456))