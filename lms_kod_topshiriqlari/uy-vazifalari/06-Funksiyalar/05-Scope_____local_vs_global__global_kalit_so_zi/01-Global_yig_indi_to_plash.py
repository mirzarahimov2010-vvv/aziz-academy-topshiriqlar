jami = 0 

def qosh(x):
    global jami 
    jami += x 
    
    
sonlar = map(int, input().split())

for son in sonlar:
    qosh(son)
    
    
print(jami)