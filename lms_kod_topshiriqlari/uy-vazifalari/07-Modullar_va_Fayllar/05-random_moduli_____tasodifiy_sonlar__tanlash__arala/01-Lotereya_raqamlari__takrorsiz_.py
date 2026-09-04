import random 

seed_val = int(input())
n, k = map(int, input().split())

random.seed(seed_val)
result = random.sample(range(1, n + 1), k)
print(*(result))