from datetime import datetime, timedelta


t = datetime.today()
y = t - timedelta(days=1)
t1 = t + timedelta(days=1)
print(y.strftime('%Y-%m-%d'))
print(t.strftime('%Y-%m-%d'))
print(t1.strftime('%Y-%m-%d'))

d = datetime.now()
print(d.replace(microsecond=0))

a = datetime(2024, 7, 1, 12, 0, 0)
b = datetime(2024, 7, 2, 14, 30, 0)
d = a - b
d.total_seconds()