def sum_all(*args):
    return sum(args)

nums = list(map(int, input().split()))
result = sum_all(*nums)

print(result)