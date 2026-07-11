n = int(input())

d = {}

for _ in range(n):
    guruh, ball = input().split()
    d[guruh] = d.get(guruh, 0) + int(ball)
    
for guruh in sorted(d):
    print(guruh, d[guruh])