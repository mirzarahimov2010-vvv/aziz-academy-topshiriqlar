n = int(input())
sonlar = list(map(int, input().split()))
yarmi = n // 2 
birinchi_yarm = sonlar[:yarmi]
print(birinchi_yarm)