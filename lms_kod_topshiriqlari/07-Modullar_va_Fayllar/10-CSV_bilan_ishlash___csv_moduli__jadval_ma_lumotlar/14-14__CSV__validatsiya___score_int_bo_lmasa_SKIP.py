n = int(input())
s = 0 

for _ in range(n):
    name, value = input().split()
    
    if value.lstrip('-').isdigit():
        s += int(value)
        
print(s)