counter = 0 

def inc():
    global counter 
    counter += 1 
    return counter 

def reset():
    global counter 
    counter = 0 
    return 0 

q = int(input())

for _ in range(q):
    cmd = input().strip()
    
    if cmd == "inc":
        print(inc())
    elif cmd == "reset":
        print(reset())