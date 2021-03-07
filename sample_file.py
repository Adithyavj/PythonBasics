# f=open("creatfile.py","wb+") create a file
"""
f=open("creatfile.py","w")
f.write("print('Hai')")
f.close()

"""
# Read a file
with open("creatfile.py", "r") as f:
    x = f.read()

print(x)
