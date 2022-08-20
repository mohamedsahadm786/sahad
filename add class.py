class name:
    def sample(self,name):
        self.name = name
    def __add__(self, other):
        name = self.name + " " + other.name
        return name



first_name = name()
second_namr = name()
first_name.sample("mohamed")
second_namr.sample("sahad M")
final_name = first_name + second_namr
print(final_name)