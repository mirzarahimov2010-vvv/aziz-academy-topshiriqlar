import math 

x = float(input())

s = math.sin(x)
c = math.cos(x)


print(f"{s:.4f}")
print(f"{c:.4f}".replace("-0.0000", "0.0000"))