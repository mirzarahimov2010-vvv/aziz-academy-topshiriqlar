n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))
    
nums.sort()

for x in nums:
    print(x, end=" ")