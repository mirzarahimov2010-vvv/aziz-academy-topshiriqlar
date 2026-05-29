n = int(input())
yigindi = 0 
for i in range(1, n + 1):
    if i % 9 != 0:
        yigindi += i 
print(yigindi)        