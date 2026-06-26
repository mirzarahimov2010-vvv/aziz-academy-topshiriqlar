def build_stats(*args, **kwargs):
    return {
        'count': len(args),
        'min': min(args),
        'max': max(args),
        'sum': sum(args),
        'extra_keys': sorted(kwargs.keys()),
        'extra_sum': sum(kwargs.values())
   }
    
nums = list(map(int, input().split()))
n = int(input())

data = {}
for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
    
print(build_stats(*nums, **data))