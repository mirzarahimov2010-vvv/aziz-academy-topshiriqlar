import random 

seed = int(input())
n, a, b = map(int, input().split())

random.seed(seed)

mx = random.randint(a, b)

for _ in range(n - 1):
    x = random.randint(a, b)
    if x > mx:
        mx = x 
        
print(mx)