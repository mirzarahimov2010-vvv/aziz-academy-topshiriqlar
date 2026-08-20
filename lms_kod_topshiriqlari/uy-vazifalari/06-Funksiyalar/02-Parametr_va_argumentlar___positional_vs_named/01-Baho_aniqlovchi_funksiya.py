def baho(a, b, c):
    avg = (a + b + c) / 3 
    if avg >= 90:
        return "a'lo"
    elif avg >= 70:
        return "yaxshi"
    elif avg >= 60:
        return "qoniqarli"
    else:
        return "qoniqarsiz"
    
    
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

print(baho(a, b, c))