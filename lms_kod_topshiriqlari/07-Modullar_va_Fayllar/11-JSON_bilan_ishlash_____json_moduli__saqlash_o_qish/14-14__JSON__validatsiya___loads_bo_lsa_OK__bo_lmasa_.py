import json 

s = input()

try:
    json.loads(s)
    print("OK")
except:
    print("NO")
    
        