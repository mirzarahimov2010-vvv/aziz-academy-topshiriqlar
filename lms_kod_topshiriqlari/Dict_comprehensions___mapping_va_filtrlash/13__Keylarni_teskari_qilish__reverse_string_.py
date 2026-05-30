n = int(input())
result = {key[::-1]: int(value) for _ in range(n) for key, value in [input().split()]}
print(result)