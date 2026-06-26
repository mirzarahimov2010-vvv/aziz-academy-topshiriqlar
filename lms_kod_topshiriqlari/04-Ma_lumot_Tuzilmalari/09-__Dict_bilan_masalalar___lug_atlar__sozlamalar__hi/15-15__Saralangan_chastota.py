matn = input()

chastota = {}

for harf in matn:
    if harf in chastota:
        chastota[harf] += 1 
    else:
        chastota[harf] = 1 
        
for harf in sorted(chastota.keys()):
    print(f"{harf}={chastota[harf]}")