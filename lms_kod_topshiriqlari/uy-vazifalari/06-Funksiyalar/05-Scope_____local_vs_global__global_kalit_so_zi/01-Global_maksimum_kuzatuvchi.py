eng_katta = None

def tekshir(x):
    global eng_katta
    if eng_katta is None or x > eng_katta:
        eng_katta = x 
        
        
        
sonlar = list(map(int, input().split()))

for son in sonlar:
    tekshir(son)
    
print(eng_katta)