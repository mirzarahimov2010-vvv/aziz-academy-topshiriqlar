import random  
seed = int(input())
items = input().split()

random.seed(seed)

random.shuffle(items)

print(*items[:3])