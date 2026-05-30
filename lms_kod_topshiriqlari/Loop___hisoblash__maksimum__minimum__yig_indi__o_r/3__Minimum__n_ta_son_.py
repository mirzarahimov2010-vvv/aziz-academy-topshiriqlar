n = int(input())
numbers = list(map(int, input().split()))
mn = numbers[0]
for x in numbers:
    if x < mn:
        mn = x 
print(mn)