# abstract base class means - parent class gives orders to child class to defin function if you want to inherit
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 7
        self.breadth = 9
    
    # if you dont defin this method then there will be error
    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())