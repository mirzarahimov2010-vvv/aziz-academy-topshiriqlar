n = int(input())

ro_yxat = []

for _ in range(n):
    ro_yxat.append(int(input()))
    
qidirilayotgan_son = int(input())

if qidirilayotgan_son in ro_yxat:
    print("bor")
else:
    print("yo'q")