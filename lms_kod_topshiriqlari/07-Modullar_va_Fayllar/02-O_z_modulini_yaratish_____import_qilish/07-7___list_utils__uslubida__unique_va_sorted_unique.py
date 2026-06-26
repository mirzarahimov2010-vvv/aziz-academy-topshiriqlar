def unique(nums):
    return set(nums)

def sorted_unique(nums):
    return sorted(unique(nums))

nums = list(map(int, input().split()))

print(*sorted_unique(nums))