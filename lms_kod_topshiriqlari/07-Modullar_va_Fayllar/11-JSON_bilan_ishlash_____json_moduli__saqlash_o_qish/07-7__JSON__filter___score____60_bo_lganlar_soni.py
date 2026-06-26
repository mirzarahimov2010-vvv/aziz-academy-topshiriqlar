n = int(input())

cnt = 0 

for _ in range(n):
    name, score = input().split()
    if int(score) >= 60:
        cnt += 1 
        
print(cnt)  