def malumot(**kwargs):
    res = []
    for k, v in kwargs.items():
        res.append(f"{k}: {v}")
    return res 


n = int(input().strip())
d = {}
for _ in range(n):
    line = input().strip()
    if '=' in line:
        k, v = line.split('=', 1)
        d[k] = v 
        
for item in malumot(**d):
    print(item)