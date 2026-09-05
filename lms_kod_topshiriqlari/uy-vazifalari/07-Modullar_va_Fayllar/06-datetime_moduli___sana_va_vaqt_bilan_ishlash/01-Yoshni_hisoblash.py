from datetime import date 

y1, m1, d1 = map(int, input().split())

y2, m2, d2 = map(int, input().split())

birth_date = date(y1, m1,d1)
current_date = date(y2, m2, d2)

age = current_date.year - birth_date.year

if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1
    
print(age)