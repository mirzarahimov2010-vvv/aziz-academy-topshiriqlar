from datetime import date, timedelta 

y, m, d = map(int, input().split())

n = int(input())

d_obj = date(y, m, d)

new_date = d_obj + timedelta(days=n)
print(new_date.isoformat())