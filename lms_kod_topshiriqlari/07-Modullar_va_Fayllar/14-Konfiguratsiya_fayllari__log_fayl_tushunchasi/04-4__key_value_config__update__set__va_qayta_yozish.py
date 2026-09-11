config = {}

while True:
    try:
        s = input()
    except EOFError:
        break 
        
    if "=" in s:
        key, value = s.split("=", 1)
        config[key] = value 
    else:
        key = s 
        value = input()
        config[key] = value 
        
for key in sorted(config):
    print(f"{key}={config[key]}")