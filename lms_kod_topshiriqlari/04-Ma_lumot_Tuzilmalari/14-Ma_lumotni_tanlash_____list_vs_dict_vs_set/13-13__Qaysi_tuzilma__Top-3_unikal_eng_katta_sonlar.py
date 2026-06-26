nums = list(map(int, input().split()))

unique_nums = set(nums)

sorted_nums = sorted(unique_nums, reverse=True)

top3 = sorted_nums[:3]

print(*top3)