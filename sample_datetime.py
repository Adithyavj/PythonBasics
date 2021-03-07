import datetime
#package to get datetime

now=datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))
print(datetime.date.today())
print(datetime.date.today().month)

x=datetime.datetime(2020,4,12)
print(x)