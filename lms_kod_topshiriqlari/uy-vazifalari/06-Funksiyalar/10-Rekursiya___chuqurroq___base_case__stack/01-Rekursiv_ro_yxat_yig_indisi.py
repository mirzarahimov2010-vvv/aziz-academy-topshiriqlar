def royxat_yigindisi(sonlar):
    if len(sonlar) == 0:
        return 0 
    return sonlar[0] + royxat_yigindisi(sonlar[1:])
qator = input()
if qator.strip() == "":
    print(0)
else:
    sonlar = list(map(int, qator.split()))
    print(royxat_yigindisi(sonlar))
                  