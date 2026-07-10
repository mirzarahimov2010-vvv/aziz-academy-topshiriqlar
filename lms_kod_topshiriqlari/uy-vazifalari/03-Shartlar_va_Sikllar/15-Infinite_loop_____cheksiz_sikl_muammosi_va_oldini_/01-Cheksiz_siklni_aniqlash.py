start = int(input())
step = int(input())

if step <= 0:
    print("CHEKSIZ")
else:
    qadam = 0 
    while start < 100:
        start += step 
        qadam += 1
    print(qadam)