nums = [int(x) for x in input().split()]
n = len(nums)

mean = round(sum(nums) / n, 2)

nums_sorted = sorted(nums)
if n % 2 != 0:
    median = nums_sorted[n // 2]
else:
    median = (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) // 2
    
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1 
    
max_freq = max(counts.values())

modes = [k for k, v in counts.items() if v == max_freq]
mode = min(modes)

print("O'rtacha:", mean)
print("Mediana:", median)
print("Moda:", mode)