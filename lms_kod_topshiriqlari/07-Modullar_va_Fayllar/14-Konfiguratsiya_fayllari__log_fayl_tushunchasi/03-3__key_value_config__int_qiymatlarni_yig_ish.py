n = int(input())

total = 0 
for _ in range(n):
    key, value = input().split("=")
    total += int(value)
print(total) 