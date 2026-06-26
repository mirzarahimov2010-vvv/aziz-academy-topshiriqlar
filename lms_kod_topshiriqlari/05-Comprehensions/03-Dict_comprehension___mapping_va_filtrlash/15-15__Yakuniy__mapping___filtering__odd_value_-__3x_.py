n = int(input())
data = [input().split() for _ in range(n)]
result = { 
    key: (int(value) * 3 if int(value) % 2 != 0 else int(value) * 2)
    for key, value in data 
    if abs(int(value)) >= 2 
} 
print(result)