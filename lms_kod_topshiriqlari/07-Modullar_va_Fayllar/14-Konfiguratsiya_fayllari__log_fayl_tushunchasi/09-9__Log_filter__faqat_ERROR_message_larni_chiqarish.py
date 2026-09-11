n = int(input())

for _ in range(n):
    s = input().strip()
    
    if s.startswith("ERROR:"):
        print(s[6:].strip())