eng_katta = None 

while True:
    amal = int(input())
    
    if amal == 0:
        break 
        
        
    a = int(input())
    b = int(input())
    
    if amal == 1:
        natija = a + b 
    elif amal == 2:
        natija = a - b 
    elif amal == 3:
        natija = a * b 
    elif amal == 4:
        if b == 0:
            continue
            natija = a // b 
    elif amal == 5:
        natija = a ** b 
    elif amal == 6:
        if b == 0:
            continue
        natija = a % b 
    else:
        continue
        
    print(natija)
    
    if eng_katta is None or natija > eng_katta:
        eng_katta = natija 
        
print("Eng katta natija:", eng_katta)
            
            