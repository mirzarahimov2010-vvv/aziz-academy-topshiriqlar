n = int(input())
sonlar = list(map(int, input().split()))
for son in sonlar:
    if son % 5 == 0:
        print(son)