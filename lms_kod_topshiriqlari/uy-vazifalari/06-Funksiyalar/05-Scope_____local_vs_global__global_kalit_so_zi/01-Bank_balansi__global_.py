balans = 0 


def kirim(x):
    global balans
    balans += x 
    
    
def chiqim(x):
    global balans
    balans -= x 
    
n = int(input())

for _ in range(n):
    amal = input().strip()
    
    belgi = amal[0]
    qiymat = int(amal[1:])
    
    
    if belgi == "+":
        kirim(qiymat)
    elif belgi == "-":
        chiqim(qiymat)
        
print(balans)