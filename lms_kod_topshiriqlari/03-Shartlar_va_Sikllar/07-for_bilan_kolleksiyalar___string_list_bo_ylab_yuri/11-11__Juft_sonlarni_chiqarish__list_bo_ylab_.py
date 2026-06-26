n = int(input())
sonlar = list(map(int, input().split()))
for i in range(n):
    if sonlar[i] % 2 == 0:
        print(sonlar[i])