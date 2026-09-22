try:
    a = int(input())
    b = int(input())
    natija = a / b 
    
except:
    print("ERROR", end="")
else:
    print("RESULT", end="")
finally:
    print("!")