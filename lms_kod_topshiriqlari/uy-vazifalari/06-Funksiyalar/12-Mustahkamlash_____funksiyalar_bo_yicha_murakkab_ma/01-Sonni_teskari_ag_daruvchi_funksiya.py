def teskari_son(n):
    natija = 0 
    while n > 0:
        natija = natija * 10 + n % 10
        n //= 10 
    return natija


n = int(input())
print(teskari_son(n))