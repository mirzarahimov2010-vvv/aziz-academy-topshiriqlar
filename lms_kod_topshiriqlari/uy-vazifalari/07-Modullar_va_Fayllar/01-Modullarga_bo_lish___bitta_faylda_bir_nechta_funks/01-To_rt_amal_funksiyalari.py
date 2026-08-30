def qosh(a, b):
    return a + b 

def ayir(a, b ):
    return a - b 

def kopaytir(a, b):
    return a * b 

def bol(a, b):
    return a // b 

a, b = map(int, input().split())
print(qosh(a, b))
print(ayir(a, b))
print(kopaytir(a, b))
print(bol(a, b))