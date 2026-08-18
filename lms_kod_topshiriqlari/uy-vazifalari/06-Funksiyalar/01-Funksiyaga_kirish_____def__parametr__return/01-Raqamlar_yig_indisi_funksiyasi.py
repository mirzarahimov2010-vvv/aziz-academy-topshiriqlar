def raqamlar_yigindisi(n):
    yigindi = 0 
    for r in str(n):
        yigindi += int(r)
    return yigindi 

n = input()
print(raqamlar_yigindisi(n))