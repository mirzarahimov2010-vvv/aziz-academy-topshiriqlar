n = int(input())
sonlar = list(map(int, input().split()))
yigindi = sum([son for son in sonlar if son > 0])
print(yigindi)