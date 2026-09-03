def harf_sanash(soz):
    return len(soz)

def eng_uzun(sozlar):
    if not sozlar:
        return ""
    eng_uzun_soz = sozlar[0]
    for soz in sozlar:
        if len(soz) > len(eng_uzun_soz):
            eng_uzun_soz = soz 
    return eng_uzun_soz


satr = input()
sozlar_royxati = satr.split()

natija = eng_uzun(sozlar_royxati)
print(natija)
print(harf_sanash(natija))