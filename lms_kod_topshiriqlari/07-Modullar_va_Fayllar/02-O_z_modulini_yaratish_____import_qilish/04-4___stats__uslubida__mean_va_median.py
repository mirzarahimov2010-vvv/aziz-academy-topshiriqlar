def mean(nums):
    return sum(nums) / len(nums)

def median(nums):
    nums = sorted(nums)
    n = len(nums)
    
    if n % 2 == 1:
        return float(nums[n // 2])
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2 
    
nums = list(map(int, input().split()))

print(f"{mean(nums):.2f}")
print(f"{median(nums):.2f}")