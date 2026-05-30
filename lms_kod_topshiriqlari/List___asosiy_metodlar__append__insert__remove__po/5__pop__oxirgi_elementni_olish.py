n = int(input())
lst = list(map(int, input().split()))

removed = lst.pop()
print(removed)
print([*lst])