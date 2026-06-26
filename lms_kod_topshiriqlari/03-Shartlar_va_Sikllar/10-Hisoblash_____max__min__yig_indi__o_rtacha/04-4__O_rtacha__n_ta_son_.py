n = int(input())
sonlar = list(map(int, input().split()))
yigindi = 0 
count = 0 
for son in sonlar:
    yigindi += son 
    count += 1
if count > 0:
    ortacha = yigindi / count 
    print(ortacha)