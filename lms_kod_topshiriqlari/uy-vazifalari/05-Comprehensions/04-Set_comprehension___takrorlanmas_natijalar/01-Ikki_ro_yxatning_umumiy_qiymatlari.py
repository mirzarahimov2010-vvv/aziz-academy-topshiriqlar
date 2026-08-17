a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(sorted({x for x in a if x in b}))