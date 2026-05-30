n = int(input())
a = list(map(str, input().split()))
l = []
for i in a:
    if len(i)>=n:
        l.append(i)
print(l)