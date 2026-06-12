def gcd(a, b):
    while b:
        a, b = b, a % b 
    return abs(a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0 
    return abs(a * b) // gcd(a, b)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))