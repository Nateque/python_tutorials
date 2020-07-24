"""Function returning function (Closure) example"""

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power

square = to_power(2)
# print(square(6))

cube = to_power(3)
# print(cube(4))