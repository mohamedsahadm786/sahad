class member_detailes:
    year=2022
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1
    def display(self):
        print("year :"+str(member_detailes.year))
        print("name :"+self.name)
        print("age :"+str(self.age))
        print("place :"+self.place)
        print("----------------------------------------")
    @staticmethod
    def welcome():
        print("welcome")
member_detailes.welcome()
x=member_detailes("mohamed",25,"anakkayam")
y=member_detailes("sahad",20,"perimbalam")
x.display()
y.display()
print("-------------------------------------------------------------------------------------------------------------")
member_detailes.year=member_detailes.year+1
x.add_age()
x.relocate("delhi")
y.add_age()
y.relocate("banglore")
x.display()
y.display()
print("-------------------------------------------------------------------------------------------------------------")
x.add_age()
y.add_age()
member_detailes.add_year()
x.display()
y.display()