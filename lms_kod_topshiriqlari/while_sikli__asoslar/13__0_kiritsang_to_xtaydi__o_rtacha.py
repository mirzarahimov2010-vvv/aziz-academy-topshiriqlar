yigindi = 0 
soni = 0 
while True:
    x = int(input())
    if x == 0:
        break 
    yigindi += x 
    soni += 1 
if soni == 0:
    print(0)
else:
    print(yigindi / soni)