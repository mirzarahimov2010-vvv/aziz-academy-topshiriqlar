n = int(input())
sonlar = list(map(int, input().split()))
sanoq = 0 
for i in range(n):
    if sonlar[i] > 0:
        sanoq += 1 
print(sanoq)