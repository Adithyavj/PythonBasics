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


x = Students("Adi", 24, "Malappuram")
y = Students("Athulya", 17, "Melattur")
x.display()
y.display()
print("_____________________________________")
Students.year = Students.year + 1
x.add_age()
y.add_age()
x.display()
y.display()
