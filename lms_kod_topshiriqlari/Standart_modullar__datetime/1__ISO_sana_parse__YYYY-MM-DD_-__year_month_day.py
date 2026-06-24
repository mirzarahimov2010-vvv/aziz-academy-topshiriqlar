from datetime import date 

sana_satri = input().strip()

sana = date.fromisoformat(sana_satri)

print(sana.year)
print(sana.month)
print(sana.day)