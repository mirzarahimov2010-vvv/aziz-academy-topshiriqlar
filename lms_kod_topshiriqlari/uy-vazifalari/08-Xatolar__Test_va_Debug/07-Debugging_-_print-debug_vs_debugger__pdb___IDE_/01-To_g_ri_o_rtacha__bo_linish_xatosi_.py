n = int(input())

total = 0 

for _ in range(n):
    
    total += int(input())
    
avg = total / n 

print(f"{avg:.2f}")