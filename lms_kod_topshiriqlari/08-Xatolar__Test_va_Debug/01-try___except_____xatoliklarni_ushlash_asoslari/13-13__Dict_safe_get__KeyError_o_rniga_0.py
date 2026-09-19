n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = v 
    
key = input()

try:
    print(d[key])
except KeyError:
    print(0)