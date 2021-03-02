# defining a function
def hey():
    print("Hey")

# Calling the function hey!
hey()


# arbitrary argument , we can pass indefinite amount of arguments
def arbfunction(*values):
    print("Values are, First:"+values[0]+",Second: "+str(values[1]))

arbfunction("Adithya",24,"MICTCO IT Solutions")