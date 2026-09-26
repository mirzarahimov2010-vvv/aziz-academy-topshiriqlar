try:
    a = float(input())
    if 0 <= a <= 100:
        print("OK")
    else:
        print("OUT")
        
except ValueError:
    print("BAD")