nums = map(int, input().split())
res = sorted(list({(x * x) % 10 for x in nums}))
print(res)