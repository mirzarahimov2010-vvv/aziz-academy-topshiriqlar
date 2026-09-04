import random 

seed_val = int(input())
lst = input().split()

random.seed(seed_val)
random.shuffle(lst)
print(' '.join(lst))