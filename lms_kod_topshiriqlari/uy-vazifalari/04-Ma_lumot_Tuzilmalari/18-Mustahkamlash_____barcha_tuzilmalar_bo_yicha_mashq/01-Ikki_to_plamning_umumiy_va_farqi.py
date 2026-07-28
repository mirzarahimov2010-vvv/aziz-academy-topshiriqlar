set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

common = sorted(list(set1 & set2))


diff = sorted(list(set1 - set2))

print(*common)
print(*diff)