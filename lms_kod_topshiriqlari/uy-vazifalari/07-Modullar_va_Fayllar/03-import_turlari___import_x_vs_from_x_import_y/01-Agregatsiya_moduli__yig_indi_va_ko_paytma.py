def yigindi(sonlar):
    return sum(sonlar)

def kopaytma(sonlar):
    natija = 1
    for son in sonlar:
        natija *= son 
    return natija 

sonlar = list(map(int, input().split()))

print(yigindi(sonlar))
print(kopaytma(sonlar))