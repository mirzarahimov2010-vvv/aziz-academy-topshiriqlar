n = int(input())
lst = list(map(int, input().split()))

removed1 = lst.pop()
removed2 = lst.pop()

print(removed1)
print(removed2)
print([*lst])