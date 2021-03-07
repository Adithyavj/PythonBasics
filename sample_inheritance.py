class BaseClass:
    def __init__(self):
        print("Base inint")
    def set_name(self, name):
        self.name = name
        print("Base Class set_name()")


class SubClass(BaseClass):
    def __init__(self): #here this constructor overrides the constructor of base class  Constructor Overriding
        super().__init__() # if we want to call constructor of base class we use super()
        print("SubClass inint")
    def Welcome(self):
        print("Welcome")
    def set_name(self, name): #Method OverRiding base class and sub class has method of same name, the subclass method overrides the method of the base class
        super().set_name(name)
        self.name = name
        print("Sub Class set_name()")
    def display_name(self):
        print("Name: " + self.name)


y = SubClass()
y.Welcome()
y.set_name("Adithya Vijay K")
y.display_name()


#Method OverRiding
