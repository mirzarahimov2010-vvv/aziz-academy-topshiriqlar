words = input().lower().split()

d = {}
for w in words:
    d[w] = d.get(w, 0) + 1 
    
top = min(d.items(), key=lambda x: (-x[1], x[0]))

print("total:", len(words))
print("unique:", len(d))
print("top:", top[0], top[1])