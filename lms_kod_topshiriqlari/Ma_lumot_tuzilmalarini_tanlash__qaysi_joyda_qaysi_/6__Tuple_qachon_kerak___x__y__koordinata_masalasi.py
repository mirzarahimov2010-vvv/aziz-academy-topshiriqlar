n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
best = max(points, key=lambda p: (p[0], -p[1]))
print(best[0], best[1])