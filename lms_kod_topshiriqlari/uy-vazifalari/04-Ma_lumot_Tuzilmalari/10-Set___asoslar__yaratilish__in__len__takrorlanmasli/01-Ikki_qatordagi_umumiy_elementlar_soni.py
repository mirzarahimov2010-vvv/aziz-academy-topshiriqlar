a = set(map(int, input().split()))
b = set(map(int, input().split()))

count = 0 

for x in a:
    if x in b:
        count += 1
        
print(count)