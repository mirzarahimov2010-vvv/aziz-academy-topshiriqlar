n = int(input())
result = {key: abs(int(value)) for _ in range(n) for key, value in [input().split()] if abs(int(value)) >= 5}
print(result)