n = int(input())

max_ball = -1 

for _ in range(n):
    ism, ball = input().split()
    ball = int(ball)
    
    if ball > max_ball:
        max_ball = ball 
        
print(max_ball)