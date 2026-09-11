limit = int(input())
n = int(input())

error_count = 0 

for _ in range(n):
    log = input()
    if log.startswith("ERROR:"):
        error_count += 1
        
if error_count > limit:
    print("ALERT")
else:
    print("OK")