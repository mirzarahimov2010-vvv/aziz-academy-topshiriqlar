import math 

a, b, c = map(int, input().split())
D = b ** 2 - 4 * a * c 

if D < 0:
    print("Haqiqiy ildiz yo'q")
elif D == 0:
    x = -b / (2 * a)
    print(f"{x:.1f}" if f"{x:.1f}" != "-0.0" else "0.0") 
else:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1
    print(f"{x1:.1f} {x2:.1f}")