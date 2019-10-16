# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b*c
    print(p)
# Uncommenting the below line shows an error
# product(4, 5)
# This line will call
product(4, 5, 5)

class A:
    def stackoverflow(self):
        print('first method')
    def stackoverflow(self, i = "None"):
        print('second method', i)
ob=A()
ob.stackoverflow(2)