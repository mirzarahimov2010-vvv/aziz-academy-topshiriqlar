try:
    n = int(input())
    d = {}
    for _ in range(n):
        k, v = input().split()
        d[k] = int(v)
    a, b = input().split()
    
    result = d[a] // d[b]
    print(result)
    
except KeyError:
    print("NOKEY")
except ZeroDivisionError:
    print("DIV0")