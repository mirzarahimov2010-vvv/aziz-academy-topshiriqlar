def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

a, b = map(int, input().split())
print(nod(a, b))