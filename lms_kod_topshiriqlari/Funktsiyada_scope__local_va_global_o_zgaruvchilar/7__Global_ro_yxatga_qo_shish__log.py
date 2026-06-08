logs = []

def add_log(msg):
    logs.append(msg)
    
n = int(input()) 

for _ in range(n):
    msg = input()
    add_log(msg)
    
print(len(logs))
for item in logs:
    print(item)