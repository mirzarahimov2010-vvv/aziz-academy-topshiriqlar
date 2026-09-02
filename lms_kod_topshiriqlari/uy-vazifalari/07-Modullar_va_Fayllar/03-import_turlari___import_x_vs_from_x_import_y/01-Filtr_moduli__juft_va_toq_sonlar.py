def juftlar(sonlar):
    return [x for x in sonlar if x % 2 == 0]

def toqlar(sonlar):
    return [x for x in sonlar if x % 2 != 0]

sonlar = list(map(int, input().split()))

print(*(juftlar(sonlar)))
print(*(toqlar(sonlar)))