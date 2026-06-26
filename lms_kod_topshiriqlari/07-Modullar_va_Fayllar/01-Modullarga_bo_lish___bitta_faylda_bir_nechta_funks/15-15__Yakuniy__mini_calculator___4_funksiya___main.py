q = int(input())

def add(a, b):
    return a + b 

def sub(a, b):
    return a - b 

def mul(a, b):
    return a * b 

def div(a, b):
    if b == 0:
        return None 
    return a / b 

def calc(op, a, b):
    if op == "add":
        return add(a, b)
    elif op == "sub":
        return sub(a, b)
    elif op == "mul":
        return mul(a, b)
    elif op == "div":
        return div(a, b)
    
for _ in range(q):
    op, a, b = input().split()
    a = int(a)
    b = int(b)
    
    res = calc(op, a, b)
    
    if res is None:
        print("ERROR")
    elif op == "div":
        print(f"{res:.2f}")
    else:
        print(res)