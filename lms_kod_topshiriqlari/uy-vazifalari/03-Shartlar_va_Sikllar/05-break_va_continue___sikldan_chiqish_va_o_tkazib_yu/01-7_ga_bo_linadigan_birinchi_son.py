n = int(input())

found = False

for _ in range(n):
    x = int(input())
    if x % 7 == 0:
        print(x)
        found = True 
        break 
        
        
if not found:
    print("yo'q")
        