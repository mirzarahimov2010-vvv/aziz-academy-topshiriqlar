try:
    a = int(input())
    b = int(input())
    
    natija = a // b 
    
        
    print(natija)
except ZeroDivisionError:
    print("DIV0")
except ValueError:
    print("DIV0")