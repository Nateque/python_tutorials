"""Multiple Inheritance"""

class A:

    def a_method(self):
        return 'class A method'

    def hello(self):
        return 'hello class A'

class B:

    def b_method(self):
        return 'class B method'

    def hello(self):
        return 'hello class B'

class C(B,A):
    pass

c1 = C()
# print(c1.hello()) # it will print 'hello class B' 
# print(C.mro())
# print(C.__mro__)

