n = int(input())
total = n 
done = 0 
pending = 0 

for _ in range(n):
    line = input().split()
    if len(line) >= 2:
        status = int(line[1])
        if status == 1:
            done += 1 
        else:
            pending += 1
            
print(f"total {total}")
print(f"done {done}")
print(f"pending {pending}")