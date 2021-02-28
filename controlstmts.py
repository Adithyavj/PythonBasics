# if else and elif
num = input("Enter a number")

if int(num) < 0:
    print("Entered number is Negative")
elif int(num) == 0:
    print("Entered number is zero")
else:
    print("Entered Number is positive")

# Loops
i = 1
while i <= 10:
    print(i)
    i = i + 1
else:
    print("Loop Finished")
