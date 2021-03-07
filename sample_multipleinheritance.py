# Types of Inheritances
class First:
    def __init__(self):
        print("Hai")

    def display_first(self):
        print("First")

    def display(self):
        print("Display First")


class Second:
    def __init__(self):
        print("Hello")

    def display_second(self):
        print("Second")

    def display(self):
        print("Display Second")


class Third(First, Second):  # Class third inherits 2 classes first and second,
    # here inheritance in the order of class provided
    def display_third(self):
        print("Third")


x = Third()
x.display()
print(Third.mro())  # MRO : [Method Resolution Order] Shows the order in which classes will be executed
