t = int(input())
y = int(input())

if t == 1:
    narx = 1700
elif t == 2:
    narx = 1700
elif t == 3:
    narx = 4000
else:
    print("Notogri transport")
    exit()
    
if y == 1:
    print(narx)
elif y == 2:
    print(narx // 2)
elif y == 3:
    print(0)
else:
    print("Notogri toifa")