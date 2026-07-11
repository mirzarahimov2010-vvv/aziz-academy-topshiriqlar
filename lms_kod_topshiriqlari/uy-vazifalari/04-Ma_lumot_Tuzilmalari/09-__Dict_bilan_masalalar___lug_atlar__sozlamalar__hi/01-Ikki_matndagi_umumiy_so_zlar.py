line1 = input().split()
line2 = input().split()

d = {}

for word in line1:
    d[word] = 1
    
common = {}

for word in line2:
    if word in d:
        common[word] = 1
        
for word in sorted(common):
    print(word)