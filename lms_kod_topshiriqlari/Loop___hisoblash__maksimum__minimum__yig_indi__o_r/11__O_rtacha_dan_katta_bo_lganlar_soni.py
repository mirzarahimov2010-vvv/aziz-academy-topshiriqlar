n = int(input())
sonlar = list(map(int, input().split()))
average = sum(sonlar) / n 
count = 0 
for num in sonlar:
    if num > average:
        count += 1 
print(count)