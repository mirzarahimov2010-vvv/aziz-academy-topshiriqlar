n = int(input())
sozlar = {}

for _ in range(n):
    soz = input()
    if soz in sozlar:
        sozlar[soz] += 1 
    else:
        sozlar[soz] = 1 

eng_kop_soz = max(sozlar, key=sozlar.get)

print(eng_kop_soz)