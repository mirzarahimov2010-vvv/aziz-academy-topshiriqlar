import random 

seed = int(input())
n = int(input())

random.seed(seed)

alph = "abydefghijklmnopqrstuvwxsz"
dig = "0123459786"
pool = alph + dig 


password = ""

for i in range(n):
    r = random.randint(0, 35)
    password += pool[r]
    
print(password)