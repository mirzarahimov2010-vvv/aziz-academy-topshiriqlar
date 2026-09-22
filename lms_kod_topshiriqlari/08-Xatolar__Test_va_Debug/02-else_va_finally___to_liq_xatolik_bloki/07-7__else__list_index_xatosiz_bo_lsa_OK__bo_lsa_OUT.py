try:
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
        
    idx = int(input())
    val = lst[idx]
    
except (IndexError, ValueError):
    print("OUT")
else:
    print("OK")