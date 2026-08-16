nums = list(map(int, input().split()))
res = [x ** 2 for x in nums if x % 3 == 0]
print(res)