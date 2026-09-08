d = {}

n1 = int(input())
for _ in range(n1):
    parts = input().split()
    if len(parts) >= 2:
        d[parts[0]] = parts[1]
        
n2 = int(input())
for _ in range(n2):
    parts = input().split()
    if len(parts) >= 2:
        d[parts[0]] = parts[1]
        
        
for name in sorted(d.keys()):
    print(name, d[name])