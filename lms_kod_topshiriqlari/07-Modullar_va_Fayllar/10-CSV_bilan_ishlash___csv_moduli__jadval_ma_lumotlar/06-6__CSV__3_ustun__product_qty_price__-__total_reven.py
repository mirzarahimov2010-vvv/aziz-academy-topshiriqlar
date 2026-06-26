n = int(input())

jami = 0 

for _ in range(n):
    nom, miqdor, narx = input().split()
    jami += int(miqdor) * int(narx)
    
print(jami)