import datetime

def diff(a,b,c):
    x = datetime.datetime.now()
    y = datetime.datetime(a,b,c)
    if x > y:
        z = x - y
    else:
        z = y - x
    print(z.total_seconds())

a = int(input("Year?\n"))
b = int(input("Month?\n"))
c = int(input("Day?\n"))
diff(a,b,c)