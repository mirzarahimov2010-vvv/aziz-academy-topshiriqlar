nums = list(map(int, input().split()))

copy = nums[:]
copy.sort()

print(*nums)
print(*copy)