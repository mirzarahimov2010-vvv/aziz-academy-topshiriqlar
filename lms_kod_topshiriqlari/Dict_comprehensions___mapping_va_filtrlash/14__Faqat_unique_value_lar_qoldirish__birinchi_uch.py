n = int(input())
data = [input().split() for _ in range(n)]
seen_values = set()
result = {}
for key, value in data:
    val_int = int(value)
    if val_int not in seen_values:
        seen_values.add(val_int)
        result[key] = val_int
print(result)