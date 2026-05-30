def div(a, b):
    if b == 0:
        return "ERROR"
    else:
        return a /b
    
a, b = map(int, input().split())
result = div(a, b)

if result == "ERROR":
    print("ERROR")
else:
    print(f"{result:.2f}")