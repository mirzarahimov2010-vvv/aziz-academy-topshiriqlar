def eng_katta(sonlar):
    if len(sonlar) == 1:
        return sonlar[0]
    qolgan_max = eng_katta(sonlar[1:])
    return sonlar[0] if sonlar[0] > qolgan_max else qolgan_max

sonlar = list(map(int, input().split()))
print(eng_katta(sonlar))