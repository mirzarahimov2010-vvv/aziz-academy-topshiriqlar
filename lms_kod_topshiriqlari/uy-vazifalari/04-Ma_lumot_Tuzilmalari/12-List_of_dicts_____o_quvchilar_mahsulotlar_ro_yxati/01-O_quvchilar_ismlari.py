n = int(input())

o_quvchilar = []

for _ in range(n):
    ism, yosh = input().split()
    o_quvchi = {
        "ism": ism,
        "yosh": int(yosh)
    }
    o_quvchilar.append(o_quvchi)
    
for o_quvchi in o_quvchilar:
    print(o_quvchi["ism"])