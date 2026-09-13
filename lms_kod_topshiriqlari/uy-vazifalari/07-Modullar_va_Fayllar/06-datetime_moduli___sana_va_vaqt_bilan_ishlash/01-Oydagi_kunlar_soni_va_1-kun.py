from datetime import datetime, timedelta

year, month = map(int, input().split())

first_day = datetime(year, month, 1)

if month == 12:
    next_month_first = datetime(year + 1, 1, 1)
else:
    next_month_first = datetime(year, month + 1, 1)
    
last_day = next_month_first - timedelta(days=1)
days_count = last_day.day 

days_of_week = {
    0: "Dushanba",
    1: "Seshanba",
    2: "Chorshanba",
    3: "Payshanba",
    4: "Juma",
    5: "Shanba",
    6: "Yakshanba"
}

first_day_name = days_of_week[first_day.weekday()]

print(days_count)
print(first_day_name)