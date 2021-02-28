"""
 Program to print
        *
       * *
      * * *
"""
# i = int(input("Enter number of rows:"))
# j = int(input("Enter number of columns:"))
# pchr = "*"
# count=0
# while count<i:
#     count1=0
#
#     while count1<j:
#         print("*", end="")
#         count1=count1+1
#     else:
#         print("\r")
#     count=count+1
# else:
#     print("Finished")

num = int(input("rows"))
for i in range(1, num + 1):
    print(" " * (num - i) + " * " * i)
