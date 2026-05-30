n = int(input())
sonlar = list(map(int, input().split()))
musbatlar = [sum for son in sonlar if son > 0] 
print(len(musbatlar))