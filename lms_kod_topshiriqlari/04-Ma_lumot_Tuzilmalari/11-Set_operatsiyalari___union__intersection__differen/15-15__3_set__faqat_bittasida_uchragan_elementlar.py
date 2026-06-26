A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
only_once = (A - B - C) | (B - A - C) | (C - A - B)
result = sorted(only_once)
if result:
    print(*result)
else:
    print("BO'SH")
    