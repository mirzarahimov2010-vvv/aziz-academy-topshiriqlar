n = int(input())

total = 0 
i = 0 

while i < n:
    x = int(input())
    
    if x <= 0:
        i += 1
        continue
        
    total += x 
    i += 1
    
print(total)