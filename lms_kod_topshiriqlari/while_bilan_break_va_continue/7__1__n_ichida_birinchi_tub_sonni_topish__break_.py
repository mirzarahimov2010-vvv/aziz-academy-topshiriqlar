n = int(input())
if n < 2:
    print("No")
else:
    for son in range(2, n + 1):
        tub = True 
        for i in range(2, int(son ** 0.5) + 1):
            if son % i == 0:
                tub = False 
                break
        if tub:
                print(son)
                break