n = int(input())

eng_katta = int(input())
pozitsiya = 1

for i in range(2, n + 1):
    son = int(input())
    if son > eng_katta:
        eng_katta = son 
        pozitsiya = i 
        
print(pozitsiya)