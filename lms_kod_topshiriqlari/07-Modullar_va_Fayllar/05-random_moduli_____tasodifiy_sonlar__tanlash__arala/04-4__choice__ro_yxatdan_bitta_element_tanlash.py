import random 

seed = int(input())
words = input().split()

random.seed(seed)
print(random.choice(words))