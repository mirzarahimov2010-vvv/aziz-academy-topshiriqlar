yashirin = int(input())
ball = 100

while True:
    taxmin = int(input())
    
    if taxmin == yashirin:
        print("TOPDINGIZ")
        print("Ball:", ball)
        break
    elif taxmin > yashirin:
        print("KATTA")
    else:
        print("KICHIK")
        
    ball -= 10 
    if ball < 0:
        ball = 0
        