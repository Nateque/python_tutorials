# NotImplemented Error

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('Defin in subclass')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # def sound(self):
    #     return 'bhaw bhaw'

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meaoo meaoo'

dogg = Dog('dog1', 'italian')

print(dogg.sound())