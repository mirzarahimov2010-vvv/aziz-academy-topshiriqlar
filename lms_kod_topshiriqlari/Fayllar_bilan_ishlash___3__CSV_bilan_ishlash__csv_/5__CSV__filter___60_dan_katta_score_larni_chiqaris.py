n = int(input())

for _ in range(n):
    ism, ball = input().split()
    ball = int(ball)
    if ball > 60:
        print(ism, ball)