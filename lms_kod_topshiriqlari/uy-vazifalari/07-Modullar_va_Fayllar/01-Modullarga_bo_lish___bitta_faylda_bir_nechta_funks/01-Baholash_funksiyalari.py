def baho(ball):
    if ball >= 90:
        return "A"
    elif ball >= 80:
        return "B"
    elif ball >= 70:
        return "C"
    elif ball >= 60:
        return "D"
    else:
        return "F"
    
def otdimi(ball):
    if ball >= 60:
        return "otdi"
    else:
        return "yiqildi"
    
ball = int(input())

print(baho(ball))
print(otdimi(ball))