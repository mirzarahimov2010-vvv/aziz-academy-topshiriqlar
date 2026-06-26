a = list(map(int, input().split()))
print(a[0] ** (a[1] if len(a) > 1 else 2))