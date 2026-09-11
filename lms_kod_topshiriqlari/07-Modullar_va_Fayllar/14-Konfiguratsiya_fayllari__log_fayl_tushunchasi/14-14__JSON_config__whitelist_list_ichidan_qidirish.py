import json 

data = json.loads(input())
name = input()

if name in data["whitelist"]:
    print("YES")
else:
    print("NO")