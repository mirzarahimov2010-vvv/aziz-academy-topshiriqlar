n = int(input())
sonlar = list(map(int, input().split()))
for x in sonlar:
    if x > 0 and x % 2 == 0:
        print(x)