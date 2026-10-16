n = int(input())

for _ in range(n):
    
    a, b = input().split()
    
    a = int(a)
    b = int(b)
    if b == 0:
        print("xato")
    else:
        print(a // b)