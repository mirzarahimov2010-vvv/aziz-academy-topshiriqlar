import json 
s = input().strip()
if s == "":
    s = None

try: 
    json.loads(s)
    
    print("OK")
except json.JSONDecodeError:
    print("INVALID")
except TypeError:
    print("TYPE")
    