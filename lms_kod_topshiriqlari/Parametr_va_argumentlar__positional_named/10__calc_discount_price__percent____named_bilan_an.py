def discount(a, b): return a * (100 - b) / 100 
a,b = map(int, input().split())
result = discount(a, b)
print(f"{result:.2f}")
print(f"{result:.2f}")