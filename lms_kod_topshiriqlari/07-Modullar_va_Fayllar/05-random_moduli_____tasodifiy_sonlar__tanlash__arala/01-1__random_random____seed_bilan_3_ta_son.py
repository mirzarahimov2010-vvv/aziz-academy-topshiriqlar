import random 

seed = int(input())

random.seed(seed)

print(f"{random.random():.6f}")
print(f"{random.random():.6f}")
print(f"{random.random():.6f}")