def eng_katta(sonlar):
    return max(sonlar)

def eng_kichik(sonlar):
    return min(sonlar)

def diapazon(sonlar):
    return max(sonlar) - min(sonlar)

sonlar = list(map(int, input().split()))

print(eng_katta(sonlar))
print(eng_kichik(sonlar))
print(diapazon(sonlar))