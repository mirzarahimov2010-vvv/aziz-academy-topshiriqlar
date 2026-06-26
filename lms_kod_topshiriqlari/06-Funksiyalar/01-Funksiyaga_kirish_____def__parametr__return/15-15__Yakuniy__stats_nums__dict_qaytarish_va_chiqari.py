def stats(nums): return {'count':len(nums), 'sum':sum(nums), 'min':min(nums),'max':max(nums)}
print(stats(list(map(int, input().split()))))