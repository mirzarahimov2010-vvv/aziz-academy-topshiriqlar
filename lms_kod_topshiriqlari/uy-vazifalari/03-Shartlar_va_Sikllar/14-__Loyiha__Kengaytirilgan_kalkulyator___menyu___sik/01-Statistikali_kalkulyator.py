amallar = 0 
yigindi = 0 

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
        
    else:
        continue
        
    print(natija)
    amallar += 1
    yigindi += natija
    
print("Amallar:", amallar)
print("Natijalar yig'indisi:", yigindi)