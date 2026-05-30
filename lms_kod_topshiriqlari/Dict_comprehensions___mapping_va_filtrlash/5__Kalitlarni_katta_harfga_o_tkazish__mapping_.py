n = int(input())
result = {key.upper(): int(value) for _ in range(n) for key, value in [input().split()]}
print(result)