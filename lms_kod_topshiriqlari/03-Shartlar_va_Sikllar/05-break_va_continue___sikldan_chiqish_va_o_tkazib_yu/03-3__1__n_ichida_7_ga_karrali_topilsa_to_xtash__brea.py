n = int(input())
i = 1 
topildi = False 
while i <= n:
    if i % 7 == 0:
        print(i)
        topildi = True 
        break 
    i += 1 
if not topildi:
    print("No")