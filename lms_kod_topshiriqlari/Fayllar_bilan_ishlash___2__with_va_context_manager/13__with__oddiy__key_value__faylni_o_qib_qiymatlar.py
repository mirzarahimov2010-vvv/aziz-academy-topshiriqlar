n = int(input())

s = 0 

for _ in range(n):
    line = input()
    s += int(line.split('=')[1])
    
print(s)