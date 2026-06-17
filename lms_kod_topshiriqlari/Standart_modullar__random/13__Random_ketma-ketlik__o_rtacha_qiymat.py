import random 

seed = int(input())
n, a, b = map(int, input().split())

random.seed(seed)

total = 0 

for _ in range(n):
    total += random.randint(a, b)
    
mean = total / n 

print(f"{mean:.2f}")