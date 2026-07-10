nums = list(map(int, input().split()))

for son in nums:
    if son < 0:
        print(0, end=" ")
    else:
        print(son, end=" ")