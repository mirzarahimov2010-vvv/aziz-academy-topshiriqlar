def saralash(sonlar):
    return sorted(sonlar)

def mediana(sonlar):
    s = sorted(sonlar)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    
satr = input()
sonlar_royxati = [float(x) if '.' in x else int(x) for x in satr.split()]

saralangan= saralash(sonlar_royxati)
med = mediana(sonlar_royxati)

print(*(saralangan))
print(med)