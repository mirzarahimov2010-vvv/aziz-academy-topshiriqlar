n = int(input())

d = {}

for _ in range(n):
    key, value = input().split("=")
    d[key] = value 
    
print(len(d))