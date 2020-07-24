"""What is Class and creating our first class"""


class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print("init method get called")
        self.first = first_name
        self.last = last_name
        self.age = age

p1 = Person('nateq', 'siddiqui', 23)
p2 = Person('ahmed', 'gul', 26)

print(p1.first)
print(p2.last)