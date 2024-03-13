import datetime

def micro_drop():
    x = datetime.datetime.now()
    print(x.strftime('%c'))
micro_drop()