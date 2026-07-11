n = int(input())

d = {}

for _ in range(n):
    ism, baho = input().split()
    d[ism] = int(baho)
    
eng_ism = ""
eng_baho = -1

for ism, baho in d.items():
    if baho > eng_baho or (baho == eng_baho and ism <eng_ism):
        eng_baho = baho
        eng_ism = ism
        
print(eng_ism, eng_baho)