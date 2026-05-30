numbers = list(map(int, input().split()))
result_set = {abs(x) for x in numbers}
print(' '.join(map(str, sorted(result_set))))