A = set(input().strip().split())
B = set(input().strip().split())
common = sorted(A & B) 
print(len(common)) 
for name in common:
    print(name)
