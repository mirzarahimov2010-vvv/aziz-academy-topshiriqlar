n = int(input())
names = [input() for _ in range(n)]

max_len = max(len(name) for name in names)

for name in names:
    print(name.ljust(max_len) + "|")