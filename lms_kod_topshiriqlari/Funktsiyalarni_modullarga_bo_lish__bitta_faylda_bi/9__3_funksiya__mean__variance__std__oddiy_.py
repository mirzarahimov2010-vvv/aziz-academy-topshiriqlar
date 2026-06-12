import math 

nums = list(map(int, input().split()))

m = sum(nums) / len(nums)
var = sum((x- m) ** 2 for x in nums) / len(nums)
std = math.sqrt(var)

print(f"{m:.2f}")
print(f"{var:.2f}")
print(f"{std:.2f}")