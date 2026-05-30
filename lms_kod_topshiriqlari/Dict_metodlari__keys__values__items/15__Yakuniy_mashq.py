fan1, b1 = input().split()
fan2, b2 = input().split()
fan3, b3 = input().split()
b1 = int(b1)
b2 = int(b2)
b3 = int(b3)
max_fan = fan1
max_baho = b1
if b2 > max_baho:
    max_baho = b2
    max_fan = fan2
if b3 > max_baho:
    max_baho = b3 
    max_fan = fan3
print(max_fan, max_baho)