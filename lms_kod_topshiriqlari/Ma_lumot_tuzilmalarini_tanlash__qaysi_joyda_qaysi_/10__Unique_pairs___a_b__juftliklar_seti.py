A = list(map(int, input().split()))
B = list(map(int, input().split()))

pairs = set()

for a in A:
    for b in B:
        pairs.add((a, b))
        
        
result = sorted(pairs)
print(len(result))

for a, b in result:
    print(a, b)