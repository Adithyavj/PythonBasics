import datetime

start = datetime.datetime.now()

x = datetime.datetime.now()
y = datetime.datetime(year=1996, month=8, day=10)
dif = x - y
print(dif)

end = datetime.datetime.now()

difference = end - start
print(difference)
