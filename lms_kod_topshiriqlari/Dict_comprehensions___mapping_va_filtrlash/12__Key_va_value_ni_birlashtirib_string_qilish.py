n = int(input())
result = {key: f"{key}:{value}" for _ in range(n) for key, value in [input().split()]}
print(result)