n = int(input())
result = {key: int(value) * 2 for _ in range(n) for key, value in [input().split()]}
print(result)