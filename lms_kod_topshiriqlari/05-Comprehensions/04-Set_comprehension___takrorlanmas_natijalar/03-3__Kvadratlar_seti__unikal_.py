nums = list(map(int, input().split()))
squares = {x**2 for x in nums}
print(' '.join(map(str, sorted(squares))))