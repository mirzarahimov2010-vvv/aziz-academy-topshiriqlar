a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a.intersection(b)
if len(c) == 0:
    print("BO'SH")
else:
    
    print(*sorted(c))