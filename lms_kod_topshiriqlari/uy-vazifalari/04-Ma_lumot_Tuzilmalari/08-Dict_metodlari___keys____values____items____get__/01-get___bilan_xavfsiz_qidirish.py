n = int(input())

d = {}

for _ in range(n):
    mahsulot, son = input().split()
    d[mahsulot] = int(son)
    
qidir = input()

print(d.get(qidir, "Topilmadi"))