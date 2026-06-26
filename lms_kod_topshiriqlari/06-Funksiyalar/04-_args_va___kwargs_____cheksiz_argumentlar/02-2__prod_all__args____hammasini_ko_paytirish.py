def prod_all(*args):
    result = 1 
    for num in args:
        result *= num 
    return result 

nums = list(map(int, input().split()))

result = prod_all(*nums)

print(result)