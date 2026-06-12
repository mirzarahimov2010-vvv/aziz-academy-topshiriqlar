line = input()

def parse_ints(line):
    return list(map(int, line.split()))

def unique(nums):
    return list(set(nums))

def sort_nums(nums):
    
    
    return sorted(nums)

nums = parse_ints(line)
nums = unique(nums)
nums = sort_nums(nums)

print(*nums)