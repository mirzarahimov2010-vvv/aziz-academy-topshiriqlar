data = {}

while True:
    line = input().strip()
    
    if "=" not in line:
        key = line 
        break 
        
    name, value = line.split("=", 1)
    data[name] = value 
    
if key in data:
    print(data[key])
else:
    print("NOTFOUND")