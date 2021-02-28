# files=["Joker.mp4","Justice League.mp4","Memories.mp4"]
#
# for x in files:
#     print(x.replace(".mp4",""))

#  program to print multiplication table of a number

num = int(input("Enter Number"))
till = int(input("Multiplication table till:"))
count = 0
for i in range(0, (num * till) + 1, num):
    print(str(num) + " * " + str(count) + " = " + str(i))
    count = count + 1
