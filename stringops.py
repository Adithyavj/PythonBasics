# To get length of a string
a = "Hey, how are you"
print(len(a))
print(a[5])
print(a[5:8])  # to print from one position to another of an array

# string values are immutable

# List in python
names = ["apple", "orange", "mango"]
names[0] = "changed"  # list is mutable, values can be changed
print(names)
print(len(names))


names=names+["New Value",100]
names.append("Appended Value")
print(names)
