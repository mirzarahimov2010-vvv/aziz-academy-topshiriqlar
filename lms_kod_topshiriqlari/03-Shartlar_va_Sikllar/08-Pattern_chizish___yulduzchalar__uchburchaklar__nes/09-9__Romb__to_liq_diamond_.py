n = int(input())
for i in range(-n+1, n):
    print(' ' * abs(i) + '*' * (2*(n-abs(i))-1))