a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a.union(b)
print(len(c))