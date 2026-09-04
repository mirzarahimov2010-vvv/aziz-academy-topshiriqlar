import random 

seed_val = int(input())
royxat = input().split()

random.seed(seed_val)
print(random.choice(royxat))