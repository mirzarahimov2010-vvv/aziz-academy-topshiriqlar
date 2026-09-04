import random

seed_val = int(input())
n = int(input())

random.seed(seed_val)
for _ in range(n):
    print(random.randint(1, 6))