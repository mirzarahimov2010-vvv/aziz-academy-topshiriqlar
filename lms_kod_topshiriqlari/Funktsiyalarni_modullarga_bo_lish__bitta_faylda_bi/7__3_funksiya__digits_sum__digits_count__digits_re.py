n = int(input())

s = sum(int(d) for d in str(n))

cnt = len(str(n))

rev = int(str(n)[::-1])

print(s)
print(cnt)
print(rev)