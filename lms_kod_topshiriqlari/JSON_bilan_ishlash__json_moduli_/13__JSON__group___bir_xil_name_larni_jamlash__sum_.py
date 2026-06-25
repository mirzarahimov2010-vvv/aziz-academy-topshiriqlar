import json

n = int(input())

d = {}

for _ in range(n):
    name, score = input().split()
    score = int(score)
    
    d[name] = d.get(name, 0) + score
    
print(json.dumps(d))