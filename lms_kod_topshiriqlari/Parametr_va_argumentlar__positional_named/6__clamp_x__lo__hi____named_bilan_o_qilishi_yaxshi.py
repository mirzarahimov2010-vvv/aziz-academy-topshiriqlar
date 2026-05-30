def clamp(x, lo, hi): return lo if x < lo else hi if x > hi else x
x, lo, hi = map(int, input().split())
print(clamp(x, lo, hi))
print(clamp(lo = lo, hi = hi, x = x))