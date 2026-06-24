from datetime import date, timedelta 

sana_satri = input().strip()
kunlar = int(input().strip())

d = date.fromisoformat(sana_satri)

yangi_sana = d + timedelta(days=kunlar)

print(yangi_sana.isoformat())