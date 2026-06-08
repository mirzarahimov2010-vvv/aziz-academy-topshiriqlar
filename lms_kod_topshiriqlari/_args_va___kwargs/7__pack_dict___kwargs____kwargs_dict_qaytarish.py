def pack_dict(**kwargs):
    
    return kwargs 

n = int(input())

data = {}
for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
    
result = pack_dict(**data)

print(result)