import datetime

def five_days_ago():
    x = datetime.datetime.now()
    y = x - datetime.timedelta(days=5)
    print(y.day, y.strftime("%A"))

five_days_ago()