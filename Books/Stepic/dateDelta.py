import datetime

y, m, d = map(int, input().split())
days = int(input())

current = datetime.date(year=y, month=m, day=d)
current += datetime.timedelta(days=days)

print("{} {} {}".format(current.year, current.month, current.day))
