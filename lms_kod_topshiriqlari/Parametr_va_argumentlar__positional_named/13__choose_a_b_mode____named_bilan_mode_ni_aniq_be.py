a, b = map(int, input().split())
op = input()
if op == "max": result = a if a > b else b 
elif op == "min": result = a if a < b else b 
else: result = a 
print(result)
print(result)