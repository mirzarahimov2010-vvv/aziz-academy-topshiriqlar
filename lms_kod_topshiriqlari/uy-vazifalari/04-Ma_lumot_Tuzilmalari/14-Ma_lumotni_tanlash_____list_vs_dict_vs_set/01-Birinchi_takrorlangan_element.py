items = input().split()

seen = set()

found = False

for item in items:
    if item in seen:
        print(item)
        found = True 
        break
        
    seen.add(item)
    
if not found:
    print("yoq")