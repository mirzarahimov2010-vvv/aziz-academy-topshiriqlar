yashirin = int(input())
urinish = 0

while True:
    taxmin = int(input())
    urinish += 1 
    
    if taxmin == yashirin:
        print("TOPDINGIZ")
        break
    elif taxmin > yashirin:
        print("KATTA")
    else:
        print("KICHIK")
        
print("Urinishlar:", urinish)