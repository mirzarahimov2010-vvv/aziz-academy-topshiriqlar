words = input().split()
res = [w for w in words if w[0] in "aeiou"]
print(res)