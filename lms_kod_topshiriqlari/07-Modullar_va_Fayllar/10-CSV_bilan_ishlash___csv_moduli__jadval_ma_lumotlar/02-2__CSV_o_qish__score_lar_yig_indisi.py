n = int(input())

s = 0 
for i in range(n):
    ism, ball = input().split()
    s += int(ball) 
    
print(s)