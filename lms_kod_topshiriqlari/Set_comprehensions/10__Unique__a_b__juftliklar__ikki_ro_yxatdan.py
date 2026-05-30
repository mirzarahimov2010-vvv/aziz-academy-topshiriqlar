A = list(map(int, input().split()))
B = list(map(int, input().split()))
pairs = {(a, b) for a in A for b in B}
print(len(pairs))
sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
for a, b in sorted_pairs:
    print(f"{a},{b}")