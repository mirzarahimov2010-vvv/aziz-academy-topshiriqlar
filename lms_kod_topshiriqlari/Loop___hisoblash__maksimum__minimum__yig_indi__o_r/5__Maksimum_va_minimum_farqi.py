n = int(input())
sonlar = list(map(int, input().split()))
max_qiymat = max(sonlar)
min_qiymat = min(sonlar)
natija = max_qiymat - min_qiymat 
print(natija)