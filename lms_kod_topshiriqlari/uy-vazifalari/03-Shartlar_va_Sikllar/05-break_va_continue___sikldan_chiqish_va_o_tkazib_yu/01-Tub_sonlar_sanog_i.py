count = 0 

while True:
    n = int(input())
    
    if n == 0:
        break 
        
    if n < 2:
        continue
        
    is_prime = True 
    i = 2 
    
    while i * i <= n:
        if n % i == 0:
            is_prime = False 
            break 
            
        i += 1 
        
    if is_prime:
        count += 1 
        
print(count)