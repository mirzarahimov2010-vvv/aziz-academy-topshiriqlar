from datetime import date 

sana_satri = input().strip()

d = date.fromisoformat(sana_satri)

if d.weekday() < 5:
    print("WORKDAY")
else:
    print("WEEKEND")