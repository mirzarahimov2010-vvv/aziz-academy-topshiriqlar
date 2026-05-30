a = list(map(int, input().split()))
if len(a) == 1:
    x =a[0]
    print(max(0, min(100, x)))
    
else:
    x, low, high = a 
    print(max(low, min(high, x)))