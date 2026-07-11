soz = input()

harf = {}

for ch in soz:
    harf[ch] = harf.get(ch, 0) + 1
    
for ch in sorted(harf):
    print(ch, harf[ch])