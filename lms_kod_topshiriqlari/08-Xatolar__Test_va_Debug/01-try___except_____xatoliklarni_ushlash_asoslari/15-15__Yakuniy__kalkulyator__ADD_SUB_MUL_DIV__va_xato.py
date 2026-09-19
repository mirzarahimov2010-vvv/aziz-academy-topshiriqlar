try:
    op = input().strip()
    a = float(input())
    b = float(input())
    
    if op == "ADD":
        res = a + b 
    elif op == "SUB":
        res = a - b 
    elif op == "MUL":
        res = a * b 
    elif op == "DIV":
        if b == 0:
            print("DIV0")
        else:
            res = a / b 
            print(f"{res:.2f}")
    else:
        print("ERROR")
        
    if op != "DIV" and op in ["ADD", "SUB", "MUL"]:
        print(f"{res:.2f}")
        
        
except ZeroDivisionError:
    print("DIV0")
except ValueError:
    print("BAD")