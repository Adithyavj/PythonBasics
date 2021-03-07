# object oriented Programming

class MySampleClass:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)


# Creating an object/instance of the class

x = MySampleClass()
y = MySampleClass()
name = "Adithya Vijay K"
x.hello(name)
y.hello("Arjun")

x.print_name()
y.print_name()

#This can also be done as
#MySampleClass.hello(x) ,here x is self
