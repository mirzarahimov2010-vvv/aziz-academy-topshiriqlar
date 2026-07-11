nums = list(map(int, input().split()))


cnt = {}

for x in nums:
    cnt[x] = cnt.get(x, 0)  + 1
    
max_count = max(cnt.values())
ans = min(k for k, v in cnt.items() if v == max_count)

print(ans)