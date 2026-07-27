n = int(input())

guruhlar = {}

for _ in range(n):
    data = input().split()
    guruh_nomi = data[0]
    talabalar = data[1:]
    guruhlar[guruh_nomi] = talabalar
    
for guruh_nomi, talabalar in guruhlar.items():
    print(guruh_nomi, len(talabalar))