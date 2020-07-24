"""Class method as a constructor, to create our own constructor"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    # Static Method
    @staticmethod
    def hello():
        print("Hello, How are you?")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def above_18(self):
        return self.age > 18

p1 = Person('Nateq', 'siddiqui', 24)
p2 = Person.from_string('nateq,siddiqui,23')

print(p2.__dict__)
print(p2.full_name())

Person.hello()