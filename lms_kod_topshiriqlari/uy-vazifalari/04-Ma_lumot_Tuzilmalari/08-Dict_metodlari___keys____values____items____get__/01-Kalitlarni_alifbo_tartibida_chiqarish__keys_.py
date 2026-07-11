n = int(input())

d = {}

for _ in range(n):
    ism, baho = input().split()
    d[ism] = int(baho)
    
    
print(*sorted(d.keys()))