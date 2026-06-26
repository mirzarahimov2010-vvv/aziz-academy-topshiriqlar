n = int(input())
max_nomi = ""
max_qiymat = -1 

for _ in range(n):
    nom, miqdor, narx = input().split()
    qiymat = int(miqdor) * int(narx)
    
    if qiymat > max_qiymat:
        max_qiymat = qiymat
        max_nomi = nom 
print(max_nomi)