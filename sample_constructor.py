class Students:
    year = 2020  # Class Variable like static variable in c#

    def __init__(self, name, age, place):  # constructor of the class sampleclass
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year: " + str(Students.year))
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Place: " + self.place)

    # A function to add year+1, for this we need a class method
    @classmethod
    def add_year(cls):  # class as argument
        cls.year = cls.year + 1

    @staticmethod
    def display_welcome():
        print("Welcome")


Students.display_welcome()

print("----------------------------------------------------")
x = Students("Adi", 24, "Malappuram")
y = Students("Athulya", 17, "Melattur")
x.display()
y.display()
print("----------------------------------------------------")
Students.year = Students.year + 1
x.add_age()
y.add_age()
x.display()
y.display()
print("----------------------------------------------------")
Students.add_year()
x.add_age()
y.add_age()
x.relocate("Dubai")
y.relocate("Pala")
x.display()
y.display()
