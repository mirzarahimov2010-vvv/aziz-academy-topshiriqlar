from datetime import date 

sana_satri = input().strip()

d = date.fromisoformat(sana_satri)

print(d.strftime('%d.%m.%Y'))