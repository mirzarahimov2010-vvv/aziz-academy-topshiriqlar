n = int(input())
numbers = list(map(int, input().split()))
mx = numbers[0]
for x in numbers:
    if x > mx:
        mx = x 
print(mx)