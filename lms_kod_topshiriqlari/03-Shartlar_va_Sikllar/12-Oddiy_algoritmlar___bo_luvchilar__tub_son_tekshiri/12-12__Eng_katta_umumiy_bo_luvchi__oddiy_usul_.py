a, b = map(int, input().split())
ekub = 1 
limit = min(a, b)
for i in range(1, limit + 1):
    if a % i == 0 and b % i == 0:
        ekub = i 
print(ekub)