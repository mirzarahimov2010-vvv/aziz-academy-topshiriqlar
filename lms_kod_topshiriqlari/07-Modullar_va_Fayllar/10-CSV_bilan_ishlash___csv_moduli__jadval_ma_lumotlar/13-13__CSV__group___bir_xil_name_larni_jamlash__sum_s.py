n = int(input())

data = {}
order = []

for _ in range(n):
    name, value = input().split()
    value = int(value)
    
    if name not in data:
        data[name] = value 
        order.append(name)
    else:
        data[name] += value 
        
for name in order:
    print(name, data[name])