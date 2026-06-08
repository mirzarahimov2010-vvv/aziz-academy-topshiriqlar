def sum_named(**kwargs):
    return sum(kwargs.values())

n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
    
print(sum_named(**d))