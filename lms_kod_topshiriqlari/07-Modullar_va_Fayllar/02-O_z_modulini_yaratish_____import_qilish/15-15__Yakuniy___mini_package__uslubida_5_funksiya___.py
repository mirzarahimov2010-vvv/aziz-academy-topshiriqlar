def parse_ints(line):
    return list(map(int, line.split()))

def mean(nums):
    return sum(nums) / len(nums)

def minmax(nums):
    return min(nums), max(nums)

def count_pos_neg(nums):
    pos = sum(1 for x in nums if x > 0)
    neg = sum(1 for x in nums if x < 0)
    return pos, neg 

def report(nums):
    n = len(nums)
    m = mean(nums)
    mn, mx = minmax(nums)
    p, g = count_pos_neg(nums)
    
    return f"count={n} mean={m:.2f} min={mn} max={mx} pos={p} neg={g}"

nums = parse_ints(input())
print(report(nums))