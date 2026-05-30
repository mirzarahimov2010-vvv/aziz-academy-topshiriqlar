n = int(input())
d = {}
for _ in range(n):
    name, score = input().split()
    d[name] = score 
q = int(input())
for _ in range(q):
    name = input()
    print(d.get(name, "NOT_FOUND"))