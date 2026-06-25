n = int(input())

info = 0 
warn = 0 
error = 0 

for _ in range(n):
    s = input()
    
    if s.startswith("INFO:"):
        info += 1 
    elif s.startswith("WARN:"):
        warn += 1 
    elif s.startswith("ERROR:"):
        error += 1 
        
print("INFO", info)
print("WARN", warn)
print("ERROR", error)