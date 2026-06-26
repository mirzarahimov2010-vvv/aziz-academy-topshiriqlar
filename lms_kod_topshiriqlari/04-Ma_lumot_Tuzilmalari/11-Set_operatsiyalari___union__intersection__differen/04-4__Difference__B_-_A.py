a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = b.difference(a)
if len(c) == 0:
    print("BO'SH")
else:
    print(*sorted(c))
