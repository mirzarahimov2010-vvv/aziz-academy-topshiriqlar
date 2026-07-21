n = int(input())

oquvchilar = []
jami_baho = 0 

for _ in range(n):
    qator = input().split()
    ism = qator[0]
    baho = int(qator[1])
    oquvchilar.append({"ism": ism, "baho": baho})
    jami_baho += baho 
    
ortacha = jami_baho / n 

for o in oquvchilar:
    if o["baho"] > ortacha:
        print(o["ism"])