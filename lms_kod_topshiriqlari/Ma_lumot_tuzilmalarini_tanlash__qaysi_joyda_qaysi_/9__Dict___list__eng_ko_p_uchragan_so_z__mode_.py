words = input().split()
d = {}
for w in words:
    w = w.lower()
    d[w] = d.get(w, 0) + 1 
best = min(d.items(), key=lambda x: (-x[1], x[0]))
print(best[0], best[1])