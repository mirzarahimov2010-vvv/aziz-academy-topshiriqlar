n = int(input())
lst = list(map(int, input().split()))


removed = lst.pop(0)
print(removed)
print([*lst])