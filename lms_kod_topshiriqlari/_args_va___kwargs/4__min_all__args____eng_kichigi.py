def min_all(*args):
    return min(args)

nums = list(map(int, input().split()))

result = min_all(*nums)
print(result)