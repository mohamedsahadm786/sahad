class first:
    def display(self):
        print("first")
class second:
    def display(self):
        print("second")
class third(second,first):
    def display3(self):
        print("third")
""" we can also write :
class first:
    def display(self):
        print("first")
class second(first):
    def display(self):
        print("second")
class third(second):
    def display3(self):
        print("third")
"""
x=third()
x.display()
x.display3()
print(third.mro())
