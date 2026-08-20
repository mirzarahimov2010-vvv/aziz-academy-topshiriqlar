def kub(x):
    return x * x * x


def yigindi_kublari(n):
    jami = 0 
    for i in range(1, n + 1):
        jami += kub(i)
    return jami 


n = int(input())

print(yigindi_kublari(n))