def describe(*args, **kwargs):
    
    return {
        'args_count': len(args),
        'args_sum': sum(args),
        'kwargs_count': len(kwargs),
        'kwargs_sum': sum(kwargs.values())
   }
    
args = list(map(int, input().split()))

n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

print(describe(*args, **d))