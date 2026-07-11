total = {}

n = int(input())

for _ in range(n):
    nom, miqdor = input().split()
    total[nom] = total.get(nom, 0) + int(miqdor)
    
m = int(input())

for _ in range(m):
    nom, miqdor = input().split()
    total[nom] = total.get(nom, 0) + int(miqdor)
    
for nom in sorted(total):
    print(nom, total[nom])