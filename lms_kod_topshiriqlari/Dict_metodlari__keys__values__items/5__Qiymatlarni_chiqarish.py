n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

for value in d.values():
    print(value)