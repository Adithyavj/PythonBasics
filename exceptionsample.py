b=0

try:
    a=10/b
    print(a)
    print("Try completed")
except ZeroDivisionError:
    print("Division by zero is not possible")

print("Program executed successfully")
