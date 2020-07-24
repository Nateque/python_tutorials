""""Creating our own instance/object methods"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def is_above_18(self):
        return self.age > 18

p1 = Person('nateq', 'siddiqui', 13)

print(p1.full_name())  # it is same as ---> Person.fullname(p1)

print(p1.is_above_18())