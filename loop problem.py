"""
 Program to print
        *
       * *
      * * *
"""
i = int(input("Enter number of rows:"))
j = int(input("Enter number of columns:"))
pchr = "*"
count=0
while count<i:
    count1=0
    
    while count1<j:
        print("*", end="")
        count1=count1+1
    else:
        print("\r")
    count=count+1
else:
    print("Finished")