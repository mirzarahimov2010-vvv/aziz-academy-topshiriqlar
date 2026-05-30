n = int(input())
sonlar = list(map(int, input().split()))
for x in sonlar:
    if 0 < x < 10:
        print(x)