n = int(input())
s = 0 

for _ in range(n):
    harf, son = input().split()
    s += int(son)
print(s)