nums = list(map(int, input().split()))
t = int(input())

for son in nums:
    if son > t:
        print(son, end=" ")