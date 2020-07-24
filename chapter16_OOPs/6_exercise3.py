"""Count instances by class var and class method"""

class Person:
    objects = 0
    def __init__(self, first_name, last_name, age):
        Person.objects += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.objects} instances of {cls.__name__} Class"    

    # def count_instances(self):
    #     return Person.objects

p1 = Person('nateq', 'siddiqui', 23)
p2 = Person('Ahmed', 'Gul', 25)


print(Person.count_instances())
# print(p1.count_instances())