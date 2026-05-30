try:
    n = int(input())
    result = None
    found = False
    for i in range(n):
        row = list(map(int, input().split()))
        k = int(input())
        if i == n-1:
            if k < len(row):
                result = row[k]
                found = True 
    if not found:
        print("NONE")
    else:
        print(result)
except:
    print("BAD")
        
    
