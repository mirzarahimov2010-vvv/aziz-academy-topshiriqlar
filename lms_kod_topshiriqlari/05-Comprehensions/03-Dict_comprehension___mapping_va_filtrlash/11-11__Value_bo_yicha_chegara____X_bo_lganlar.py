n = int(input())
data = [input().split() for _ in range(n)]

X = int(input())
result = {key: int(value) for key, value in data if int(value) >= X}
print(result)