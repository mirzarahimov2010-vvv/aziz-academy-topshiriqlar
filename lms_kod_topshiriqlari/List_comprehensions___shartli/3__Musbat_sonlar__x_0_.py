a = list(map(int, input().split()))
res = [x for x in a if x > 0]
if res:
    print(*res)
else:
    print("BO'SH")