n = int(input())

mahsulotlar = {}
tartib = []

for _ in range(n):
    nom, miqdor = input().split()
    miqdor = int(miqdor)
    
    if nom not in mahsulotlar:
        mahsulotlar[nom] = miqdor
        tartib.append(nom)
    else:
        mahsulotlar[nom] += miqdor
        
for nom in tartib:
    print(nom, mahsulotlar[nom])