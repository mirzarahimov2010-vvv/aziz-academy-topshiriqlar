def normalize(nums): m=sum(nums)/len(nums); return [f"{(x-m):.2f}" for x in nums]
print(' '.join(normalize(list(map(int, input().split())))))