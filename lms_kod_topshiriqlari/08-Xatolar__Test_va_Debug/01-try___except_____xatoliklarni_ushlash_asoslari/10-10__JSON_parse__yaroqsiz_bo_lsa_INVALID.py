import json

try:
    data = input()
    json.loads(data)
    print("OK")
except json.JSONDecodeError:
    print("INVALID")