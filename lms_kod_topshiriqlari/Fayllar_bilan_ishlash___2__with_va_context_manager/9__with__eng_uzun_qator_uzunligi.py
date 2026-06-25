n = int(input())
mx = 0 

for _ in range(n):
    s = input()
    if len(s) > mx:
        mx = len(s)
        
print(mx)