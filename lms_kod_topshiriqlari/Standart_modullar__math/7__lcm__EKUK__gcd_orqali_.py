import math 

a, b = map(int, input().split())

if a == 0 or b == 0:
    print(0)
else:
    g = math.gcd(a, b)
    print(abs(a * b) // g)