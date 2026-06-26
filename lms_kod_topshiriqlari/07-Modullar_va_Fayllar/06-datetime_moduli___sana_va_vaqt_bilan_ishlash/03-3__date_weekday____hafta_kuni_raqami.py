from datetime import date
s = input()
d = date.fromisoformat(s)
print(d.weekday())