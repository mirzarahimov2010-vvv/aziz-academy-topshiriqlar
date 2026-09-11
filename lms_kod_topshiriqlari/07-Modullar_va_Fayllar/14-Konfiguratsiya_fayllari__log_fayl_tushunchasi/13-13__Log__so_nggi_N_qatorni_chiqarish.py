n = int(input())

logs = []

for _ in range(n):
    logs.append(input())
    
k = int(input())

for logs in logs[-k:]:
    print(logs)