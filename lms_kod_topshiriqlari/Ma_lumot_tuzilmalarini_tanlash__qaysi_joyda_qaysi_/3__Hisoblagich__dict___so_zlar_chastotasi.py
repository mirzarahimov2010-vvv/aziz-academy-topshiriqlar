words = input().split()
d = {}
for w in words:
    w = w.lower()
    d[w] = d.get(w, 0) + 1 
for w in sorted(d):
    print(w, d[w])