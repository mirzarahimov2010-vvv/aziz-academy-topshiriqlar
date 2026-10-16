n = int(input())

nums = []

for _ in range(n):
    
    nums.append(int(input()))
mx = nums[0]
for x in nums:
    if x > mx:
        mx = x 
print(mx)