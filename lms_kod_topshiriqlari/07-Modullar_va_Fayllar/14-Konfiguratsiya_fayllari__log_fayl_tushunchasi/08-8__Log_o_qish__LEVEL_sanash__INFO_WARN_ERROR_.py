n = int(input())

info = 0 
warn = 0 
error = 0 

for _ in  range(n):
    log = input().strip()
    
    if log.startswith("INFO"):
        info += 1
    elif log.startswith("WARN"):
        warn += 1
    elif log.startswith("ERROR"):
        error += 1 
        
print("INFO", info)
print("WARN", warn)
print("ERROR", error)