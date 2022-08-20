import datetime
now=datetime.datetime.now()
print(datetime.datetime.now())
print(datetime.date.today())
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d-%m-%y"))
x=datetime.datetime(2012,day=3,month=2)
y=datetime.datetime(2012,day=2,month=2)
print(x-y)
end=datetime.datetime.now()
d=end-now
print(d)