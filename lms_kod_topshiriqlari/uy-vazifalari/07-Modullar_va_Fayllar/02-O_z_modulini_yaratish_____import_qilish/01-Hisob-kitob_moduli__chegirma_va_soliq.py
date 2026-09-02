def chegirma(narx, foiz):
    return narx * (100 - foiz) // 100 

def soliqli(narx):
    return narx + narx * 12 // 100 

narx, foiz = map(int, input().split())
print(soliqli(chegirma(narx, foiz)))