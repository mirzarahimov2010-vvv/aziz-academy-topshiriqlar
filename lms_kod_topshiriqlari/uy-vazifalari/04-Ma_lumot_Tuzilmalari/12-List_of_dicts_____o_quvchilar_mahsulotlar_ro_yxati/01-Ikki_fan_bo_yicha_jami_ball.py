n = int(input())
oquvchilar = []

for _ in range(n):
    data = input().split()
    ism = data[0]
    mat = int(data[1])
    fiz = int(data[2])
    
    
    oquvchilar.append({
        "ism": ism,
        "mat": mat,
        "fiz": fiz
    })
    
for talaba in oquvchilar:
    jami = talaba["mat"] + talaba["fiz"]
    print(f"{talaba['ism']} {jami}")