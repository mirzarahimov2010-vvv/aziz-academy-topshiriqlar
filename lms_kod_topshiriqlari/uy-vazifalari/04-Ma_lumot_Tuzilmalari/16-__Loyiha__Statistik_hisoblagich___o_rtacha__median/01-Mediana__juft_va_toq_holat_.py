nums = [int(x) for x in input().split()]

nums.sort()

n = len(nums)

if n % 2 != 0:
    print(nums[n // 2 ])
    
else:
    left_mid = nums[n // 2 - 1]
    right_mid = nums[n // 2]
    print((left_mid + right_mid) // 2)