list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

common = sorted(list1 & list2)

print(*common)