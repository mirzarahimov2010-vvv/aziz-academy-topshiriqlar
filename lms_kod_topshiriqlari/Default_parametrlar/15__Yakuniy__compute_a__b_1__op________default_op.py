def compute(a, b = 1, op='+'):
    if op == '+':
        return a + b 
    elif op == '-':
        return a - b 
    elif op == '*':
        return a * b 
    elif op == '/':
        if b == 0:
            return "ERROR"
        return a / b 
tokens = input().strip().split()

if len(tokens) == 1:
    a = float(tokens[0])
    result = compute(a)
elif len(tokens) == 2:
    a = float(tokens[0])
    b = float(tokens[1])
    result = compute(a, b)
else:
    a = float(tokens[0])
    b = float(tokens[1])
    op = tokens[2]
    result = compute(a, b, op)
    
if result == "ERROR":
    print("ERROR")
elif isinstance(result, float) and result != int(result):
    print(f"{result:.2f}")
else:
    print(int(result))