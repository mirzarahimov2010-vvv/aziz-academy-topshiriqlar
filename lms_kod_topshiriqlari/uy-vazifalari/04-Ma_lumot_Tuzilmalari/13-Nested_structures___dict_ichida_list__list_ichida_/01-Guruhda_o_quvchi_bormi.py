n = int(input())
guruhlar = {}

for _ in range(n):
    data = input().split()
    guruh_nomi = data[0]
    ismlar = data[1:]
    guruhlar[guruh_nomi] = ismlar
    
target_guruh, target_ism = input().split()

if target_ism in guruhlar[target_guruh]:
    print("Ha")
else:
    print("Yoq")