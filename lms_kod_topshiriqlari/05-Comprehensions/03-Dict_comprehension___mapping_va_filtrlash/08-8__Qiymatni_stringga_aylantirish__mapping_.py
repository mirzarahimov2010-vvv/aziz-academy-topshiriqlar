n = int(input())
result = {key: str(value) for _ in range(n) for key, value in [input().split()]}
print(result)