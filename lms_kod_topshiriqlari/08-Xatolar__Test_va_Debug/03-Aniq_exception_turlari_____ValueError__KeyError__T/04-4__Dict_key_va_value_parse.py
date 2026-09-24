try:
    n = int(input())
    d = {}
    for _ in range(n):
        parts = input().split()
        if len(parts) == 2:
            key, val = parts 
            d[key] = int(val) 
    search_key = input().strip()
    print(d[search_key])
except KeyError:
    print("NOKEY")
except ValueError:
    print("BADVAL")
except Exception:
    print("BADVAL")