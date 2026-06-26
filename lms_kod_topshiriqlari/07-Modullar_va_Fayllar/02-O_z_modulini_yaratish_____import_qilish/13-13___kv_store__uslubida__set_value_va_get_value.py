store = {}

def set_value(key, val):
    store[key] = val 
    
def get_value(key, default=None):
    return store.get(key, default)

q = int(input())

for _ in range(q):
    parts = input().split()
    
    if parts[0] == "set":
        set_value(parts[1], parts[2])
    else:
        result = get_value(parts[1])
        print(result if result is not None else "NONE")