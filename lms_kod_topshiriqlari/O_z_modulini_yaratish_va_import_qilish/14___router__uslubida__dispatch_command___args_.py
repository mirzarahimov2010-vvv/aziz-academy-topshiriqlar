def add(a, b):
    return a + b 

def mul(a, b):
    return a * b 

def pow(a, b):
    return a ** b 

def dispatch(cmd, *args):
    if cmd == "add":
        return add(*args)
    elif cmd == "mul":
        return mul(*args)
    elif cmd == "pow":
        return pow(*args)
    
    
q = int(input())

for _ in range(q):
    cmd, a, b = input().split()
    a, b = int(a), int(b)
    print(dispatch(cmd,a,b))