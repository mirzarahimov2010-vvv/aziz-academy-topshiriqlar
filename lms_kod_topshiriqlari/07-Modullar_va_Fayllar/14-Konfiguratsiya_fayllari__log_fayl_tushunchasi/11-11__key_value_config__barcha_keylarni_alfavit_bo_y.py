n = int(input())

names = []

for _ in range(n):
    line = input()
    name = line.split("=")[0]
    names.append(name)
    
names.sort()

for name in names:
    print(name)