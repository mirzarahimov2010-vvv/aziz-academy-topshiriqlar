n = int(input())

birinchi = int(input())
eng_katta = birinchi 
eng_kichik = birinchi

for i in range(n - 1):
    son = int(input())
    if son > eng_katta:
        eng_katta = son 
    if son < eng_kichik:
        eng_kichik = son 
        
print(eng_katta - eng_kichik) 