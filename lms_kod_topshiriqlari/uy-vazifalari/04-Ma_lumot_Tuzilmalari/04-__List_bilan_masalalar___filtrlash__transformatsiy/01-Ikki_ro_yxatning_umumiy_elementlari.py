a = input().split()
b = input().split()

natija = []

for x in a:
    if x in b and x not in natija:
        natija.append(x)
        
print(*natija)