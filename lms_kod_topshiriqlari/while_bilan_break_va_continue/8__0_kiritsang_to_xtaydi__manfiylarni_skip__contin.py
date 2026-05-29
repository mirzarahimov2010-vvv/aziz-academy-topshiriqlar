yigindi = 0 
while True:
    son = int(input())
    if son == 0:
        break
    if son < 0:
        continue
    yigindi += son 
print(yigindi)