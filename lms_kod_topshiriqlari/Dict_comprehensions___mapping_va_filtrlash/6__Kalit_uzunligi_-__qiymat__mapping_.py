n = int(input())
result = {len(key): int(value) for _ in range(n) for key, value in [input().split()]}
print(result)