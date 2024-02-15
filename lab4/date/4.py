import datetime

a = datetime.datetime(2013,12,30,23,59,59)
b = datetime.datetime(2013,12,31,23,59,59)

print((b-a).total_seconds())    