from datetime import date 

sana1_satri = input().strip()
sana2_satri = input().strip()

d1 = date.fromisoformat(sana1_satri)
d2 = date.fromisoformat(sana2_satri)

print((d2 - d1).days)