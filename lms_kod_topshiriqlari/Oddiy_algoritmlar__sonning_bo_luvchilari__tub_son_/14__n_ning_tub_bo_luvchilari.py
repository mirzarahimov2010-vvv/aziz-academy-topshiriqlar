n = int(input())
print("")
for i in range(2, n + 1):
    if n % i == 0:
        tub = True 
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                tub = False 
                break 
        if tub:
            print(i)