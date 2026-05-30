n = int(input())
result = {key: 'even' if int(value) % 2 == 0 else 'odd' for _ in range(n) for key, value in [input().split()]}
print(result)