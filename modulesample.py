# Importing a module, this is done by using keyword import

import checknumber
# To import only one function from a module we can use from checknumer import checkposneg

value=int(input("Enter a value"))
checknumber.checkposneg(value)


# another way of calling a function in a module

check=checknumber.checkposneg
check(10)