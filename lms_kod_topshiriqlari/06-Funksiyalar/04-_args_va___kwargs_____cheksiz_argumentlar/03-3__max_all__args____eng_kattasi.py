def max_all(*args):
    
    return max(args)

nums = list(map(int, input().split()))

result = max_all(*nums)

print(result)