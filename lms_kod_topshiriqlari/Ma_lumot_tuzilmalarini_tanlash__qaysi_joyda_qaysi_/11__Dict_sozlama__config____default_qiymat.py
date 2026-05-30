k = int(input())

config = {}

for _ in range(k):
    key, value = input().split()
    config[key] = int(value)
    
q = int(input())

for _ in range(q):
    key = input().strip()
    print(config.get(key, 0))
    