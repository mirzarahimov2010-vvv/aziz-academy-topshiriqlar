s = input().strip()
a, b = map(int, s.split())
total = 0 
for i in range(a, b + 1):
    total += i 
print(total)