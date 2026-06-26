nums = list(map(int, input().split()))
unique_nums = {x for x in nums}
print(' '.join(map(str, sorted(unique_nums))))