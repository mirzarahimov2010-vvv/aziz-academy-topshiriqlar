r = int(input())

jami = 0 
eng_yaxshi = 0 

for i in range(1, r + 1):
    yashirin = int(input())
    urinish = 0 
    
    while True:
        taxmin = int(input())
        urinish += 1 
        
        if taxmin == yashirin:
            break 
            
            
    print(f"Round {i}: {urinish} urinish")
    
    jami += urinish
    
    if i == 1 or urinish < eng_yaxshi:
        eng_yaxshi = urinish
        
print(f"Jami: {jami}")
print(f"Eng yaxshi: {eng_yaxshi}")