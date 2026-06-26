def max2(a, b):
    return a if a > b else b 

a, b = map(int, input().split())
print(max2(a, b))