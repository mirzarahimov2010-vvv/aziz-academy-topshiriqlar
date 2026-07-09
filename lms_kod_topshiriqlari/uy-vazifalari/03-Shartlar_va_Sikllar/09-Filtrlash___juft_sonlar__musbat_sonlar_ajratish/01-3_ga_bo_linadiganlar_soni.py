n = int(input())
count = 0 

for i in range(n):
    son = int(input())
    if son % 3 == 0:
        count += 1
        
print(count) 