amallar = {
    "+": lambda a, b: a +b,  
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b 
}


qator = input().split()
a = int(qator[0])
amal = qator[1]
b = int(qator[2])

print(amallar[amal](a, b))