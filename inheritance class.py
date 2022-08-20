class baseclass:
    def __init__(self,name):
        self.name=name
        print("name :"+name)
    def check_class(self):
        print("it is from base class")

class subclass(baseclass):
    def __init__(self):
        super().__init__("mohamed")
# or here we can write like this - baseclass.__init__(self,"mohamed")
        print("      sahad\n      madathodiyil")
    def prin(self):
        print("sahad M")
    def disp(self):
        print("name :"+self.name)
    def check_class(self):
# Also we can run the function check_class in the baseclass,we can code like this:
        super().check_class()
        print("it is from sub class")
y = subclass()
y.check_class()


