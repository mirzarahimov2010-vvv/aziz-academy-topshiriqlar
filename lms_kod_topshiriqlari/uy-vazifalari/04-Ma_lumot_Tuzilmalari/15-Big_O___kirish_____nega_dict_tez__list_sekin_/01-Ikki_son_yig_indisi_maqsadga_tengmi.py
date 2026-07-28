numbers = [int(x) for x in input().split()]

target = int(input())

seen = set()
found = False 

for x in numbers:
    if (target - x) in seen:
        found = True 
        break
        
    seen.add(x)
    
if found:
    print("Ha")
else:
    print("Yoq")