n = int(input())

total = 0 

for _ in range(n):
    name, score = input().split()
    total += int(score)
    
print(total)