n = int(input())
total = 0 

for _ in range(n):
    try:
        val = int(input())
        total += val 
    except ValueError:
        pass 
print(total)