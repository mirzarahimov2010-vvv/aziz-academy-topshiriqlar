import random 

seed = int(input())
random.seed(seed)

nums = random.sample(range(1, 50), 6)

    
nums.sort()
print(*nums)
