n = int(input())
sonlar = list(map(int, input().split()))
max_count = 0 
mode = sonlar[0]
for i in range(n):
    count = 0 
    for j in range(n):
        if sonlar[j] == sonlar[i]:
            count += 1 
            if count > max_count or (count == max_count and sonlar[i] < mode):
                max_count = count 
                mode = sonlar[i]
print(mode)