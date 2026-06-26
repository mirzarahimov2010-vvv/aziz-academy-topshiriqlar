n = int(input())
sonlar_toplami = set()

for _ in range(n):
    sonlar_toplami.add(int(input()))
    
qidirilayotgan_son = int(input())

print(qidirilayotgan_son in sonlar_toplami)