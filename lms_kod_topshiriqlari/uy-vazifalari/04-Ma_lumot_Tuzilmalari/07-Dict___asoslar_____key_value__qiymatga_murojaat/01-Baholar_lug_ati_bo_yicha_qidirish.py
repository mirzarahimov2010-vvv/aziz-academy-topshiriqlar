n = int(input())
d = {}

for i in range(n):
    ism, baho = input().split()
    d[ism] = baho
    
qidir = input()

print(d[qidir])