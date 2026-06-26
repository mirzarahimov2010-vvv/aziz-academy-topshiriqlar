import json 

d = json.loads(input())

keys = sorted(d.keys())
print(*[d[k] for k in keys])