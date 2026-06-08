def config_get(key, default=None, **kwargs):
    return kwargs.get(key, default)

qidir = input()
n = int(input())

data = {}

for _ in range(n):
    k, v = input().split()
    data[k] = int(v)
    
print(config_get(qidir, default=0, **data))