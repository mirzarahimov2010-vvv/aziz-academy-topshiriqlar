n = int(input())
result = {key: int(value) for _ in range(n) for key, value in [input().split()] if key.startswith('a')}
print(result)