n = int(input())

mahsulotlar = []
for _ in range(n):
    nom, narx = input().split()
    mahsulotlar.append({"nom": nom, "narx": int(narx)})
    
limit = int(input())

for m in mahsulotlar:
    if m["narx"] < limit:
        print(m["nom"])