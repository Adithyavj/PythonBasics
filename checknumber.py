#this is a module

print("Module name is : "+__name__) #prints the name of this module

print("Default value called when we import this module")

def checkposneg(number):
    if(number<0):
        print("Negative value")
    elif (number==0):
        print("Number is Zero")
    else:
        print("Positive Value")
