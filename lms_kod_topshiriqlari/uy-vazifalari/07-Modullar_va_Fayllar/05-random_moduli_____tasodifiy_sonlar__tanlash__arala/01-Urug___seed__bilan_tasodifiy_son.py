import random 

seed_val = int(input())
a, b = map(int, input().split())

random.seed(seed_val)
print(random.randint(a, b))