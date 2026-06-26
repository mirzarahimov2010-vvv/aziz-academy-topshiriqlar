def pick(**kwargs):
    return {k: v for k, v in kwargs.items() if v > 0}

n = int(input())
data = {}

for _ in range(n):
    k, v = input().split()
    data[k] = int(v)
    
print(pick(**data))