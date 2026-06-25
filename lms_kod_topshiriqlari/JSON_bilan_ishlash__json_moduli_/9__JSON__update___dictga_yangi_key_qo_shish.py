import json 

obj = json.loads(input())
key = input()
value = input()

obj[key] = value 

print(json.dumps(obj, sort_keys=True))