"""Define function to create generator of even numbers"""

def generators(n):
    # yield [i for i in range(1,n+1) if i%2 == 0]
    for i in range(2, n+1, 2):
        yield i

value = generators(10)

for sum in value:
    print(sum)

for i in value:
    print(i)