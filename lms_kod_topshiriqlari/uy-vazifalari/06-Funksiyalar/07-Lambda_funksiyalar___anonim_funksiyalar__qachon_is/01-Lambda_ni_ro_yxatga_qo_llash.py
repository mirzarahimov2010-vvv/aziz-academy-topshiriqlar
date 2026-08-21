f = lambda x: x * x + 1

sonlar = map(int, input().split())
print(*(f(x) for x in sonlar))