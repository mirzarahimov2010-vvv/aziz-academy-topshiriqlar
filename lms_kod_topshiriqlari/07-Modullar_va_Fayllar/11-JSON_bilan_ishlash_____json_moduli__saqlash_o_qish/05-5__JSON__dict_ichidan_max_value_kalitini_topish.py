import json 
d = json.loads(input())

max_key = None 
max_val = None 

for k, v in d.items():
    
    if max_val is None or v > max_val:
        max_val = v 
        max_key = k 
        
print(max_key) 