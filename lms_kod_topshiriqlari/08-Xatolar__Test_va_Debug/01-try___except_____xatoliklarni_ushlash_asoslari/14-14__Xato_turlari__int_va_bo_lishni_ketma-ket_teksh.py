try:
    
    a = int(input())
    b = int(input())
    print(a // b)
    
except ZeroDivisionError:
    print("DIV0")
except ValueError:
    print("BAD")