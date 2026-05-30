n = int(input())
sonlar = list(map(int, input().split()))
x = int(input())
sonlar = [son for son in sonlar if son != x]
print(sonlar)