n = int(input())
result = {key: int(value) for _ in range(n) for key, value in [input().split()] if int(value) > 10} 
print(result)