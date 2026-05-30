n = int(input())
sonlar = list(map(int, input().split()))
for x in sonlar:
    if x % 2 == 0 or x < 0:
        print(x)