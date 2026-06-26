n = int(input())
max_divisor = 0 
for i in range(n // 2, 0, -1):
    if n % i == 0:
        max_divisor = i 
        break 
print(max_divisor)