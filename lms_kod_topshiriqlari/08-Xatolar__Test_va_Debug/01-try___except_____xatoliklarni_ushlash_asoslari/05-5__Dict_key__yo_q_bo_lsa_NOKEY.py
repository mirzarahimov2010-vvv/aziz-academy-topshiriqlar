n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v 
    
key = input()

if key in d:
    print(d[key])
else:
    print("NOKEY")