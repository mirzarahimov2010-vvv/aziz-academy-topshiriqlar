n = int(input())
sonlar = list(map(int, input().split()))
eng_kichik = sonlar[0] 
for i in range(1, n):
    if sonlar[i] < eng_kichik:
        eng_kichik = sonlar[i]
print(eng_kichik)