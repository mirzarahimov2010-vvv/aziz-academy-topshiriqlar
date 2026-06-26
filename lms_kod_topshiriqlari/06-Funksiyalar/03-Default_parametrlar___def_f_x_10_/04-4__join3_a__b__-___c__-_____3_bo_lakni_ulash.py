a = input().split()
while len(a) < 3:
    a.append('-')
    
print(*a[:3])