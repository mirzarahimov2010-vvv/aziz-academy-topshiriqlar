n, m = map(int, input().split())
x = int(input())
topildi = False 
for i in range(1, n + 1):
    if x % i == 0:
        j = x // i 
        if 1 <= j <= m:
            topildi = True 
            break 
print("Yes" if topildi else "No")