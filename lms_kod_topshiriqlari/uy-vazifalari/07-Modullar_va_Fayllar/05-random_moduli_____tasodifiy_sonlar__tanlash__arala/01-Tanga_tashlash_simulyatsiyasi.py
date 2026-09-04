import random 

seed_val = int(input())
n = int(input())

random.seed(seed_val)
gerb = 0 
raqam = 0 

for _ in range(n):
    if random.randint(0, 1) == 1:
        gerb += 1
    else:
        raqam += 1 
        
print(gerb, raqam)