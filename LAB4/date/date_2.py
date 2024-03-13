import datetime

def days():
    x = datetime.datetime.now()
    w = datetime.timedelta(days=1)
    y = x - w
    z = x + w
    print(x.strftime("%A"), y.strftime("%A"), z.strftime("%A"))

days()