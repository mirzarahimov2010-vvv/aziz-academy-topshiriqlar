import math

x1, y1, x2, y2 = map(int, input().split())
distance = math.hypot(x2 - x1, y2 - y1)
print(round(distance, 2))