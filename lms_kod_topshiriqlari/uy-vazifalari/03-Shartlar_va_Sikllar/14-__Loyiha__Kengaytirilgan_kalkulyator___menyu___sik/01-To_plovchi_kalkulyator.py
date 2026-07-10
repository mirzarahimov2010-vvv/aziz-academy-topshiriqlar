natija = 0 
while True:
    amal = input()
    
    if amal == "=":
        print(natija)
        break
        
        
    son = int(input())
    
    if amal == "+":
        natija += son
    elif amal == "-":
        natija -= son
    elif amal == "*":
        natija *= son
    elif amal == "/":
        if son != 0:
            natija //=son