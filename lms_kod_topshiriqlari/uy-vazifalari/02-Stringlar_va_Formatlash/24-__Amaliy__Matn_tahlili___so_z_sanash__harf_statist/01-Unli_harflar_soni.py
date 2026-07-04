matn = input().lower()
unlilar = "aeiou"

soni = 0 

for u in unlilar:
    soni += matn.count(u)
print(soni)