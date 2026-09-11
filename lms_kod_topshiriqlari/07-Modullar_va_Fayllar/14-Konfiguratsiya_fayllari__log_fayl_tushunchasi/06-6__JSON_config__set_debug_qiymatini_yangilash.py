import json 
data = json.loads(input())
debug = input().lower() == "true"

data["app"]["debug"] = debug 

print(json.dumps(data))