n = int(input())
count = 0 
i = 1 
found = False 
while i <= n:
    if i % 2 == 0:
        count += 1
        if count == 3:
            print(i)
            found = True 
            break 
    i += 1 
if not found:
    print("No")
           